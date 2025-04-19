# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "packaging==23.1",
#   "urllib3==2.0.5",
# ]
# ///

#!/usr/bin/env python3

import re
import subprocess
import urllib.request
from packaging.version import parse as parse_version
from pathlib import Path


def get_latest_rumdl_version():
    url = "https://pypi.org/pypi/rumdl/json"
    with urllib.request.urlopen(url) as response:
        data = response.read()
    import json

    releases = json.loads(data)["releases"]
    versions = sorted(
        (parse_version(v) for v in releases if not parse_version(v).is_prerelease),
        reverse=True,
    )
    return str(versions[0])


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
    latest_version = get_latest_rumdl_version()
    print(f"Latest rumdl version: {latest_version}")

    changed = False
    if update_pyproject_toml(latest_version):
        print("Updated pyproject.toml")
        changed = True
    if update_readme_md(latest_version):
        print("Updated README.md")
        changed = True

    if changed:
        subprocess.run(["git", "add", "pyproject.toml", "README.md"], check=True)
        subprocess.run(["git", "commit", "-m", f"Mirror: {latest_version}"], check=True)
        subprocess.run(["git", "tag", f"v{latest_version}"], check=True)
        print(f"Committed and tagged v{latest_version}")
    else:
        print("No changes needed.")


if __name__ == "__main__":
    main()
