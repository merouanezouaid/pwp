import sys

from pip._internal.cli.main import main as pip
from pwp.utils.requirements_manager import add_requirement, rm_requirement


def install(args,unknown_args):
    if len(sys.argv) < 3:
        print("Usage: pwp install <package_name1> [<package_name2> ...]")
        return
    pip_args = ['install'] + args.packages + unknown_args
    pip(pip_args)
    add_requirement(package_names=args.packages,
                    requirements_file=args.req_file)

def uninstall(args,unknown_args):
    if len(sys.argv) < 3:
        print("Usage: pwp uninstall <package_name1> [<package_name2> ...]")
        return
    pip_args = ['uninstall', '-y'] + args.packages + unknown_args
    pip(pip_args)
    rm_requirement(package_names=args.packages,
                   requirements_file=args.req_file)