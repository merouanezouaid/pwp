import sys
from .commands import pwp_install, pwp_uninstall


def main():
    if len(sys.argv) < 2:
        welcome_message = r"""

    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
    ░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░       ░▒▓█████████████▓▒░░▒▓█▓▒░        


    Pip With Packages - by Kaito

    Thanks for installing PWP!
    Usage:
        pwp install <package1> [<package2> ...]
        pwp uninstall <package1> [<package2> ...]

    Enjoy managing your packages with ease!
        """
        print(welcome_message)

        return

    command = sys.argv[1]

    if command == 'install':
        pwp_install()
    elif command == 'uninstall':
        pwp_uninstall()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
