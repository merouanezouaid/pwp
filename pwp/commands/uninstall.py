import os
import sys
from pip._internal.cli.main import main as pip_main
from .utils import load_packages, dump_packages, get_installed_package_version


def update_requirements(packages: dict[str, str | None]):
    requirements_file = 'requirements.txt'

    if os.path.exists(requirements_file):
        existing_packages = load_packages(requirements_file, show_versions=True)

        packages_to_remove = {
            pkg: ver for pkg, ver in packages.items()
            if pkg in existing_packages and (ver is None or existing_packages[pkg] == ver)
        }

        remaining_packages = {
            pkg: ver for pkg, ver in existing_packages.items()
            if pkg not in packages_to_remove
        }

        dump_packages(remaining_packages, requirements_file)

        if packages_to_remove:
            formatted_packages = [
                f"{pkg}=={ver}" if ver else pkg for pkg, ver in packages_to_remove.items()
            ]
            print(f"Removed {', '.join(formatted_packages)} from {requirements_file}")

        not_found = [
            f"{pkg}=={ver}" if ver else pkg for pkg, ver in packages.items() if existing_packages.get(pkg, "") != ver
        ]

        if not_found:
            print(f"Packages not found in {requirements_file}: {', '.join(not_found)}")
    else:
        print(f"{requirements_file} not found")


def pwp_uninstall():
    if len(sys.argv) < 3:
        print("Usage: pwp uninstall <package_name1> [<package_name2> ...]")
        return

    packages = sys.argv[2:]
    pip_main(['uninstall', '-y'] + packages)

    # Convert package names to a dictionary <name, version>
    packages_to_remove = {}
    for package in packages:
        name, *rest = package.split("==")
        if "==" in package:
            version = rest[0]
            packages_to_remove[name] = version
        else:
            packages_to_remove[name] = get_installed_package_version(name)

    update_requirements(packages_to_remove)
