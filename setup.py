from setuptools import setup, find_packages

setup(
    name='osintaam',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # List of dependencies
    entry_points={
        'console_scripts': [],  # List of console scripts
    },
    # Additional metadata
    author='Your Name',
    author_email='your.email@example.com',
    description='Description of your package',
    url='https://github.com/bly1535999-svg/osintaam',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)