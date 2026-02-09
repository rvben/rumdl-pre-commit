# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "packaging==23.1",
#   "urllib3==2.0.5",
# ]
# ///

#!/usr/bin/env python3

import json
import os
import re
import subprocess
import sys
import time
import urllib.request
from packaging.version import parse as parse_version
from pathlib import Path


def get_latest_rumdl_version():
    url = "https://pypi.org/pypi/rumdl/json"
    with urllib.request.urlopen(url) as response:
        data = response.read()

    releases = json.loads(data)["releases"]
    versions = sorted(
        (parse_version(v) for v in releases if not parse_version(v).is_prerelease),
        reverse=True,
    )
    return str(versions[0])


def wait_for_pypi(version, max_wait=300, interval=15):
    """Wait until the version is available on PyPI. Returns True if available."""
    url = f"https://pypi.org/pypi/rumdl/{version}/json"
    elapsed = 0
    while elapsed < max_wait:
        try:
            with urllib.request.urlopen(url) as response:
                if response.status == 200:
                    print(f"Version {version} is available on PyPI.")
                    return True
        except urllib.error.HTTPError:
            pass
        print(f"Waiting for {version} on PyPI... ({elapsed}s/{max_wait}s)")
        time.sleep(interval)
        elapsed += interval
    print(f"Timed out waiting for {version} on PyPI after {max_wait}s.")
    return False


def update_pyproject_toml(version):
    pyproject_path = Path("pyproject.toml")
    content = pyproject_path.read_text()
    # Replace any rumdl entry in the dependencies list with the new pinned version
    new_content = re.sub(
        r'"rumdl([<>=!~]*[0-9\.\*]*)?"', f'"rumdl=={version}"', content
    )
    if new_content != content:
        pyproject_path.write_text(new_content)
        return True
    return False


def update_readme_md(version):
    readme_path = Path("README.md")
    if not readme_path.exists():
        return False
    content = readme_path.read_text()
    new_content = re.sub(r"rev: v[\d\.]+", f"rev: v{version}", content)
    if new_content != content:
        readme_path.write_text(new_content)
        return True
    return False


def main():
    # Use version from dispatch payload if available, otherwise query PyPI
    version = os.environ.get("DISPATCH_VERSION")
    if version:
        print(f"Using version from dispatch payload: {version}")
        if not wait_for_pypi(version):
            sys.exit(1)
    else:
        version = get_latest_rumdl_version()
        print(f"Latest rumdl version from PyPI: {version}")

    changed = False
    if update_pyproject_toml(version):
        print("Updated pyproject.toml")
        changed = True
    if update_readme_md(version):
        print("Updated README.md")
        changed = True

    if changed:
        subprocess.run(["git", "add", "pyproject.toml", "README.md"], check=True)
        subprocess.run(["git", "commit", "-m", f"Mirror: {version}"], check=True)
        subprocess.run(["git", "tag", f"v{version}"], check=True)
        print(f"Committed and tagged v{version}")
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()
