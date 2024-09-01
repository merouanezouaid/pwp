import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Python package manager wrapper")
    parser.add_argument(
        "--req-file", 
        type=str, 
        default="requirements.txt",
        help="Specify the name of the requirements file (default: requirements.txt)"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands :\n\tpwp install <package1> [<package2> ...]\n\tpwp uninstall <package1> [<package2> ...]")

    # Install command
    install_parser = subparsers.add_parser("install", help="Install packages")
    install_parser.add_argument("packages", nargs="+", help="Package(s) to install")
    

    # Uninstall command
    uninstall_parser = subparsers.add_parser("uninstall", help="Uninstall packages")
    uninstall_parser.add_argument("packages", nargs="+", help="Package(s) to uninstall")

    return parser
    
