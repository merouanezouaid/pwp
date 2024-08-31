import os
import sys
from pip._internal.cli.main import main as pip_main
import importlib.metadata


def get_installed_package_version(package_name):
    """Get the installed version of a package."""
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None


def create_or_update_requirements(packages: dict[str, str | None]):
    requirements_file = 'requirements.txt'

    if os.path.exists(requirements_file):
        with open(requirements_file, 'r') as lines:
            existing_packages = {}
            for line in lines:
                line = line.strip()
                if "==" not in line:
                    existing_packages[line] = None
                else:
                    name, version = line.split("==")
                    existing_packages[name] = version
    else:
        existing_packages = {}

    updated_packages = existing_packages.copy()

    # Update or add new packages with their versions
    for package, version in packages.items():
        if version:
            updated_packages[package] = version
        elif package not in existing_packages:
            updated_packages[package] = None

    with open(requirements_file, 'w') as f:
        f.write(
            "\n".join([
                f"{package}=={version}" if version else f"{package}"
                for package, version in updated_packages.items()
            ])
        )

    added_or_updated = [f"{pkg}=={ver}" if ver else pkg for pkg, ver in packages.items()]
    print(f"Updated {requirements_file} with {', '.join(added_or_updated)}")


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
    installed_packages = {
        pkg: get_installed_package_version(pkg) if include_version else None for pkg in packages
    }

    create_or_update_requirements(installed_packages)
