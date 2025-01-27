# build with 'python setup.py build_ext --inplace'
from setuptools import setup, Extension

module = Extension(
    'c_ext',
    sources=['c_ext/c_ext.c']
)

setup(
    name='c_ext',
    ext_modules=[module]
)
