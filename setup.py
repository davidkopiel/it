from setuptools import setup, find_packages

setup(
    name='your_package_name',  # Replace with your package name
    version='0.1.0',  # Replace with your package version
    author='Your Name',  # Replace with your name
    author_email='your_email@example.com',  # Replace with your email
    description='A brief description of your package',
    long_description=open('README.md').read(),  # Optional
    long_description_content_type='text/markdown',  # Optional
    url='https://github.com/yourusername/yourproject',  # Optional
    packages=find_packages(),  # Automatically find packages
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Specify your Python version requirement
    install_requires=[
        'requests==2.31.0',  # Use the latest non-vulnerable version
        'jinja2==2.10',  # Vulnerable to XSS (CVE-2019-10906)
        'jfrog-curation-malicious-dummy==0.0.1',
        'apache-beam',
        'pytest==7.2.1',
        'pytest-timeout==2.1.0',
        'pytest-order==1.0.1',
        'cython',
        'setuptools',
        'pyinstaller',
        'graphviz',
        'ply',
        'pexpect',
        'pid',
        'psutil',
        'munch',
        'flake8',
        'click',
        'black',
        'distro',
        'fallocate',
        'humanfriendly',
        'coloredlogs',
        'lief',
    ],
)
