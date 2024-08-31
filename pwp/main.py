import os
import sys
from pip._internal.cli.main import main as pip_main

def create_or_update_requirements(package_names, action='install'):
    requirements_file = 'requirements.txt'
    
    if action == 'install':
        if not os.path.exists(requirements_file):
            with open(requirements_file, 'w') as f:
                for package in package_names:
                    f.write(f"{package}\n")
            print(f"Created {requirements_file} and added {', '.join(package_names)}")
        else:
            with open(requirements_file, 'r') as f:
                existing_packages = set(line.strip() for line in f)
            
            new_packages = [pkg for pkg in package_names if pkg not in existing_packages]
            
            if new_packages:
                with open(requirements_file, 'a') as f:
                    for package in new_packages:
                        f.write(f"{package}\n")
                print(f"Added {', '.join(new_packages)} to {requirements_file}")
            
            existing = set(package_names) & existing_packages
            if existing:
                print(f"Packages already in {requirements_file}: {', '.join(existing)}")
    
    elif action == 'uninstall':
        if os.path.exists(requirements_file):
            with open(requirements_file, 'r') as f:
                packages = set(line.strip() for line in f)
            
            packages_to_remove = set(package_names) & packages
            remaining_packages = packages - packages_to_remove
            
            with open(requirements_file, 'w') as f:
                for package in remaining_packages:
                    f.write(f"{package}\n")
            
            if packages_to_remove:
                print(f"Removed {', '.join(packages_to_remove)} from {requirements_file}")
            
            not_found = set(package_names) - packages
            if not_found:
                print(f"Packages not found in {requirements_file}: {', '.join(not_found)}")
        else:
            print(f"{requirements_file} not found")

def pwp_install():
    if len(sys.argv) < 3:
        print("Usage: pwp install <package_name1> [<package_name2> ...]")
        return

    package_names = sys.argv[2:]
    pip_main(['install'] + package_names)
    create_or_update_requirements(package_names, 'install')

def pwp_uninstall():
    if len(sys.argv) < 3:
        print("Usage: pwp uninstall <package_name1> [<package_name2> ...]")
        return

    package_names = sys.argv[2:]
    pip_main(['uninstall', '-y'] + package_names)
    create_or_update_requirements(package_names, 'uninstall')

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