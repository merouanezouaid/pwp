import argparse
import os
from pip._internal.cli.main import main as pip_main
from .utils import load_packages, dump_packages, get_installed_package_version, format_packages, filter_packages


def get_install_parser():
    parser = argparse.ArgumentParser(description="Install Python packages.", add_help=False)
    parser.add_argument(
        'packages',
        nargs='+',
        help="List of packages to install."
    )
    parser.add_argument(
        '--v',
        action='store_true',
        help="Include package versions in the output."
    )
    return parser


def create_or_update_requirements(packages: dict[str, str | None]):
    requirements_file = 'requirements.txt'

    existing_packages = load_packages(requirements_file) if os.path.exists(requirements_file) else {}

    updated_packages = existing_packages.copy()

    # Update or add new packages with their versions
    for package, version in packages.items():
        if version:
            updated_packages[package] = version
        elif package not in existing_packages:
            updated_packages[package] = None

    dump_packages(updated_packages, requirements_file)

    new_packages = filter_packages(
        packages=packages,
        condition=lambda pkg, ver: pkg not in existing_packages or existing_packages[pkg] != ver
    )

    if new_packages:
        print(f"Updated {requirements_file} with {', '.join(format_packages(new_packages))}")
    else:
        print(f"All libraries already exist in {requirements_file}. No updates made.")


def pwp_install(args):
    packages, include_version = args.packages, args.v
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
