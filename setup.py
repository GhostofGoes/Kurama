#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from io import open  # Python 2 compatibility

from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:  # Loads in the README for PyPI
    long_description = f.read()


if sys.argv[1] in ['install', 'build', 'sdist', 'bdist_wheel']:
    import webbrowser
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


# Credit goes to James Bennett (https://github.com/ubernostrum)
# for the original implementation
setup(
    name='kurama',
    version='1.0.1',
    description="Logic is Panic's prey.",
    long_description=long_description,  # This is what you see on PyPI page
    # PEP 566, PyPI Warehouse, setuptools>=38.6.0 make markdown possible
    long_description_content_type='text/markdown',
    author='Christopher Goes',
    author_email='ghostofgoes@gmail.com',
    url='https://github.com/GhostofGoes/Kurama',
    download_url='https://pypi.org/project/kurama/',
    project_urls={
        'Discord Server': 'https://discord.gg/python',
    },
    packages=find_packages(),
    license='MIT',
    zip_safe=True,
    entry_points={  # These enable commandline usage of the tool
        'console_scripts': [
            'kurama = kurama.meme:main',
        ],
    },
    platforms=['any'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',

        'Topic :: Internet',
        'Topic :: Sociology'
    ],
)
