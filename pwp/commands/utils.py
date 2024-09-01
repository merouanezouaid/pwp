import importlib.metadata


def get_installed_package_version(package_name):
    """Get the installed version of a package."""
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None


def load_packages(file, show_versions=False):
    packages = {}
    with open(file, 'r') as lines:
        for line in lines:
            line = line.strip()
            if "==" not in line:
                packages[line] = get_installed_package_version(lines) if show_versions else None
            else:
                name, version = line.split("==")
                packages[name] = version
    return packages


def dump_packages(packages, file):
    with open(file, 'w') as f:
        f.write(
            "\n".join([
                f"{package}=={version}" if version else f"{package}"
                for package, version in packages.items()
            ])
        )
