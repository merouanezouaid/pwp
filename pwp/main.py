import sys
from pwp.utils.pwp_manager import install, uninstall
from pwp.utils.pwp_parser import create_parser

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

    parser = create_parser()
    args, unknown_args = parser.parse_known_args()
        
    if args.command == "install":
        install(args, unknown_args)
    elif args.command == "uninstall":
        uninstall(args, unknown_args)
    else:
        parser.print_help()
