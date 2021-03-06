from setuptools import setup, find_packages

setup(
    name='mapcreator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Colorama',
    ],
    entry_points='''
        [console_scripts]
        mapcreator=mapcreator.cli:cli
    ''',
)
    
