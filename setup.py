from distutils.core import setup

setup(
    name = 'tranSEAt',
    version = '1.0',
    description = 'Public Transport data for the city of Naples',
    author = 'Giancarlo B.',
    packages = [
        'tranSEAt',
        'tranSEAt/shared',
        'tranSEAt/eav',
        'tranSEAt/anm',
        'tranSEAt/trenitalia',
        'tranSEAt/data'
    ],
    package_data = {
        'tranSEAt/data': ['*.json']
    },
    install_requires = [
        'requests',
        'matplotlib',
        'mplleaflet'
    ]
)