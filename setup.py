# import distutils.ccompiler
# import distutils.sysconfig
# from distutils.core import setup, Extension
import os
import sys
from setuptools import setup, Extension

# if sys.version < '2.7': 
#       tests_require.append('unittest2') 

# compiler  = distutils.ccompiler.new_compiler()
# search_paths=[os.path.expanduser('~/%s'), '/opt/local/%s', '/usr/local/%s', '/usr/%s']
# lib_paths = [ a % "lib" for a in search_paths]
# inc_paths = [ a % "include" for a in search_paths]

uclmodule = Extension('ucl',
        # include_dirs = inc_paths,
        # library_dirs = lib_paths,
        libraries = ['ucl'],
        sources = ['src/uclmodule.c'],
        # runtime_library_dirs = lib_paths,
        language='c')

setup(name='ucl',
    version='0.8',
    description='ucl parser and emmitter',
    ext_modules = [uclmodule],
    test_suite='tests',
    author="Eitan Adler, Denis Volpato Martins",
    author_email="lists@eitanadler.com",
    url="https://github.com/vstakhov/libucl/",
    license="MIT",
    classifiers=["Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: DFSG approved",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: C",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries",
        ]
    )
