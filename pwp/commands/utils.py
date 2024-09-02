import importlib.metadata
from typing import Callable


def get_installed_package_version(package_name):
    """Get the installed version of a package."""
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None


def format_packages(packages: dict[str, str | None]) -> list[str]:
    return [
        f"{package}=={version}" if version else package
        for package, version in packages.items()
    ]


def filter_packages(packages: dict[str, str | None], condition: Callable[[str, str], bool]):
    return {
        package: version for package, version in packages.items() if condition(package, version)
    }


def load_packages(file, show_versions=False):
    packages = {}

    with open(file, 'r') as lines:
        for line in lines:
            name, *rest = line.strip().split("==")
            print(line)
            if "==" not in line:
                packages[name] = get_installed_package_version(name) if show_versions else None
            else:
                version = rest[0]
                packages[name] = version
    return packages


def dump_packages(packages, file):
    with open(file, 'w') as f:
        f.write("\n".join(format_packages(packages)))
