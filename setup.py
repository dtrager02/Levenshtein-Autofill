from setuptools import setup
from Cython.Build import cythonize

setup(
    name='edits',
    ext_modules=cythonize("editDistance2.py"),
    zip_safe=False,
)