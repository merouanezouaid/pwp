import os
from pip._internal.cli.main import main as pip_main
import subprocess

def get_package_version(package):
    if "==" in package:
        return package
    try:
        # Run `pip show <package>` to get the version
        result = subprocess.run(['pip', 'show', package], capture_output=True, text=True, check=True)
        output = result.stdout
        for line in output.splitlines():
            if line.startswith('Version:'):
                print(f"{package} version: {line.split(':', 1)[1].strip()}")
                return f"{package}=={line.split(':', 1)[1].strip()}"
    except subprocess.CalledProcessError as e:
        print(f"Error getting version for {package}: {e}")
        return package

def add_requirement(package_names, requirements_file = 'requirements.txt'):
    if not os.path.exists(requirements_file):
        with open(requirements_file, 'w') as f:
            for package in package_names:
                f.write(f"{get_package_version(package)}\n")
        
        print(f"Created {requirements_file} and added {', '.join(package_names)}")
    else:
        with open(requirements_file, 'r') as f:
            existing_packages = set(line.strip() for line in f)
        
        new_packages = [pkg for pkg in package_names if pkg not in existing_packages]
        
        if new_packages:
            with open(requirements_file, 'a') as f:
                for package in new_packages:
                    f.write(f"{get_package_version(package)}\n")
            print(f"Added {', '.join(new_packages)} to {requirements_file}")
        
        existing = set(package_names) & existing_packages
        if existing:
            print(f"Packages already in {requirements_file}: {', '.join(existing)}")

def rm_requirement(package_names, requirements_file = 'requirements.txt'):
    if os.path.exists(requirements_file):
        with open(requirements_file, 'r') as f:
            packages = set(line.strip().split("==")[0] for line in f)
        
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
