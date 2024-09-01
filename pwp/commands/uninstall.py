import argparse
import os
import sys
from pip._internal.cli.main import main as pip_main
from .utils import load_packages, dump_packages, get_installed_package_version, format_packages, filter_packages


# Function to create the argument parser for the uninstall command
def get_uninstall_parser():
    parser = argparse.ArgumentParser(description="Uninstall Python packages.", add_help=False)
    parser.add_argument(
        'packages',
        nargs='+',
        help="List of packages to uninstall."
    )
    return parser


def update_requirements(packages: dict[str, str | None]):
    requirements_file = 'requirements.txt'

    if os.path.exists(requirements_file):
        existing_packages = load_packages(requirements_file)

        packages_to_remove = filter_packages(
            packages=packages,
            condition=lambda pkg, ver: pkg in existing_packages
        )

        remaining_packages = filter_packages(
            packages=existing_packages,
            condition=lambda pkg, ver: pkg not in packages_to_remove
        )

        dump_packages(remaining_packages, requirements_file)

        if packages_to_remove:
            print(f"Removed {', '.join(format_packages(packages_to_remove))} from {requirements_file}")

        not_found = filter_packages(
            packages=packages,
            condition=lambda pkg, ver: pkg not in existing_packages
        )

        if not_found:
            print(f"Packages not found in {requirements_file}: {', '.join(format_packages(not_found))}")
    else:
        print(f"{requirements_file} not found")


def pwp_uninstall(packages):
    pip_main(['uninstall', '-y'] + packages)

    # Convert package names to a dictionary <name, version>
    packages_to_remove = {}
    for package in packages:
        name, *_ = package.split("==")
        packages_to_remove[name] = None

    update_requirements(packages_to_remove)
