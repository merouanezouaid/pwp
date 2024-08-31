import os
import sys
from pip._internal.cli.main import main as pip_main


def update_requirements(packages: dict[str, str | None]):
    requirements_file = 'requirements.txt'

    if os.path.exists(requirements_file):
        with open(requirements_file, 'r') as f:
            lines = f.readlines()
            existing_packages = dict()
            for line in lines:
                line = line.strip()
                if "==" not in line:
                    existing_packages[line] = None
                else:
                    name, version = line.split("==")
                    existing_packages[name] = version

        packages_to_remove = set(packages) & set(existing_packages)
        remaining_packages = {
            pkg: ver for pkg, ver in existing_packages.items() if pkg not in packages_to_remove
        }

        with open(requirements_file, 'w') as f:
            f.write(
                "\n".join([
                    f"{package}=={version}" if version else f"{package}"
                    for package, version in remaining_packages.items()
                ])
            )

        if packages_to_remove:
            print(f"Removed {', '.join(packages_to_remove)} from {requirements_file}")

        not_found = set(packages) - set(existing_packages)
        if not_found:
            print(f"Packages not found in {requirements_file}: {', '.join(not_found)}")
    else:
        print(f"{requirements_file} not found")


def pwp_uninstall():
    if len(sys.argv) < 3:
        print("Usage: pwp uninstall <package_name1> [<package_name2> ...]")
        return

    package_names = sys.argv[2:]
    pip_main(['uninstall', '-y'] + package_names)

    # Convert package names to a dictionary with None as the version
    packages_to_remove = {pkg: None for pkg in package_names}
    update_requirements(packages_to_remove)
