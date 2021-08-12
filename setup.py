
#!/usr/bin/env python
import re
import os
from setuptools import setup, find_packages

with open('./requirements.txt', 'r') as reqs_file:
    reqs = reqs_file.readlines()

# Get version
# with open(os.path.join('epsagon', 'constants.py'), 'rt') as consts_file:
#     version = re.search(r'__version__ = \'(.*?)\'', consts_file.read()).group(1)

setup(
    name='epsagoncli',
    version='0.0.1',
    description='Epsagon CLI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Epsagon',
    author_email='support@epsagon.com',
    url='https://github.com/epsagon/epsagon-cli',
    # packages=find_packages(exclude=('tests', 'examples')),
    packages=['epsagoncli'],
    package_data={'epsagon': ['*.pem']},
    install_requires=reqs,
    license='MIT',
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest'],
    entry_points={
        'console_scripts': ['epsagoncli = epsagoncli.__main__:run']
    },
    keywords=[
        'serverless',
        'microservices',
        'epsagon',
        'tracing',
        'distributed-tracing',
        'lambda',
        'aws-lambda',
        'debugging',
        'monitoring'
    ],
    classifiers=(
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    )
)
