"""
pyip-reflector
--------------

A dead-simple IP reflector written in Python.
"""

from setuptools import setup

setup(
    name='pyip-reflector',
    version='0.1',
    license='MIT',
    author='Fred Hatfull',
    author_email='fred.hatfull@gmail.com',
    description='A dead-simple IP reflector written in Python.',
    url='https://github.com/fhats/pyip-reflector',
    packages=['pyip_reflector'],
    platforms='any',
    install_requires=[
        "Flask",
    ],
    entry_points={
    },
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
