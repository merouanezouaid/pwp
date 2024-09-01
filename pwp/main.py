import argparse
from .commands.install import get_install_parser, pwp_install
from .commands.uninstall import get_uninstall_parser, pwp_uninstall


ascii_art = r"""
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░       ░▒▓█████████████▓▒░░▒▓█▓▒░
"""


def main():
    # Set up the main argument parser
    parser = argparse.ArgumentParser(
        description=f"{ascii_art}\nPip With Packages - by Kaito\n\nThanks for installing PWP!\n",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Enjoy managing your packages with ease!"
    )

    # Create subparsers for 'install' and 'uninstall'
    subparsers = parser.add_subparsers(dest='command', help="Command to execute")

    # Install parser imported from install.py
    install_parser = get_install_parser()
    subparsers.add_parser('install', parents=[install_parser], help="Install packages")

    # Uninstall parser imported from uninstall.py
    uninstall_parser = get_uninstall_parser()
    subparsers.add_parser('uninstall', parents=[uninstall_parser], help="Uninstall packages")

    args = parser.parse_args()

    if args.command == 'install':
        pwp_install(args.packages, args.v)
    elif args.command == 'uninstall':
        pwp_uninstall(args.packages)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
