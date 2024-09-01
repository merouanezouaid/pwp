from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
import os
import sys

def run_welcome_script():
    os.system(f"{sys.executable} {os.path.join(os.path.dirname(__file__), 'pwp_welcome.py')}")

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        run_welcome_script()

class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        run_welcome_script()


setup(
    name='pwp',
    version='0.2.1',
    packages=find_packages(),
    install_requires=[
        'pip',
    ],
    entry_points={
        'console_scripts': [
            'pwp=pwp.main:main',
        ],
    },
    author='Kaito',
    author_email='kaito.collabs@gmail.com',
    description='a pip wrapper that automatically manages requirements.txt',
    long_description=open('README.md').read(),
    packages=find_packages(),
    long_description_content_type='text/markdown',
    url='https://github.com/merouanezouaid/pwp',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    }
)