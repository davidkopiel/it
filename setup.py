from setuptools import setup, find_packages

setup(
    name='frogbotTest',                          # Replace with your project name
    version='0.1.0',                           # Version of your project
    description='A brief description of your project',  # Short description
    long_description=open('README.md').read(), # Long description from README file
    long_description_content_type='text/markdown',  # Content type of long description
    author='Your Name',                        # Your name
    author_email='your.email@example.com',     # Your email address
    url='https://github.com/BiggieFudge/frogbotTest',  # Your project's repository URL
    packages=find_packages(),                   # Automatically find packages
    python_requires='>=3.6',                    # Python version requirement
    install_requires=[                          # List your project dependencies
        'Flask',
        'requests==2.27.0',
        'jinja2',
        'jfrog-curation-malicious-dummy',
    ],
)
