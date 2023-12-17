from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np
include_dirs = [np.get_include()]



extensions = [
    Extension(
        "C_code.wrapper",
        ["C_code/wrapper.pyx"],
        # extra_compile_args=['-fopenmp'],
        # extra_link_args=['-fopenmp'],
        ),

]


# extensions = ["seasonality_q3/stahl_internal/cy_loess.pyx"]


setup(
    ext_modules=cythonize(
        extensions, 
        annotate=True, 
        language_level=3,
        ),
    include_dirs=include_dirs
)

# python setup.py build_ext --inplace

# some libraries might require dynamic linking 
## http://docs.cython.org/en/latest/src/tutorial/external.html