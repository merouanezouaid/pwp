def load_packages(file):
    packages = {}
    with open(file, 'r') as lines:
        for line in lines:
            line = line.strip()
            if "==" not in line:
                packages[line] = None
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
