from setuptools import setup, find_packages

setup(
    name='openmod_example_module',
    version='1.0.0',
    description='An example module for OpenMod',
    author='Péter Törös',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'openmod-example=src.index:main'
        ]
    }
)