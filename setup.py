#!/usr/bin/env python
from setuptools import setup, find_packages

from cookie_policy import VERSION


setup(
    name='django-cookie_policy',
    version=VERSION,
    url='https://github.com/dcosentino/django-cookie-policy',
    description=(
        "Application for managing visitors consent with respect to the cookies law"),
    long_description=open('README.rst').read(),
    keywords="Django, Cookie policy, Cookie law",
    license=open('LICENSE').read(),
    platforms=['linux'],
    packages=find_packages(exclude=['sandbox*', 'tests*']),
    include_package_data=True,
    install_requires=[],
    extras_require={},
    # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Other/Nonlisted Topic'],
)