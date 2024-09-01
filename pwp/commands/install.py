import os
import sys
from pip._internal.cli.main import main as pip_main
from .utils import load_packages, dump_packages, get_installed_package_version


def create_or_update_requirements(packages: dict[str, str | None]):
    requirements_file = 'requirements.txt'

    if os.path.exists(requirements_file):
        existing_packages = load_packages(requirements_file)
    else:
        existing_packages = {}

    updated_packages = existing_packages.copy()

    # Update or add new packages with their versions
    for package, version in packages.items():
        if version:
            updated_packages[package] = version
        elif package not in existing_packages:
            updated_packages[package] = None

    dump_packages(updated_packages, requirements_file)

    new_packages = [
        f"{pkg}=={ver}" if ver else pkg for pkg, ver in packages.items()
        if pkg not in existing_packages or existing_packages[pkg] != ver
    ]

    if new_packages:
        print(f"Updated {requirements_file} with {', '.join(new_packages)}")
    else:
        print(f"All libraries already exist in {requirements_file}. No updates made.")


def pwp_install():
    if len(sys.argv) < 3:
        print("Usage: pwp install <package_name1> [<package_name2> ...] [--v]")
        return

    packages = sys.argv[2:]
    include_version = '--v' in packages

    if include_version:
        packages.remove('--v')

    pip_main(['install'] + packages)

    # Retrieve the installed versions if --v flag is present, else set versions to None
    installed_packages = {}
    for package in packages:
        name = package.split("==")[0]
        if "==" in package or include_version:
            installed_packages[name] = get_installed_package_version(name)
        else:
            installed_packages[name] = None

    create_or_update_requirements(installed_packages)
