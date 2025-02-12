from setuptools import setup, find_packages

setup(
    name='unittest-project',
    version='0.1.0',
    packages=find_packages(include=['sources', 'sources.*']),
    install_requires=[
        'coverage',
    ],
    python_requires='>=3.6',
)