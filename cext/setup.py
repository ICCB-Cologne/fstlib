from setuptools import Extension, setup
from Cython.Build import cythonize

setup(

    ext_modules = cythonize([
        Extension("pywrapfst", 
        ["pywrapfst.pyx"], 
        libraries=["fst", "fstfar", "fstscript", "fstfarscript"],
        extra_compile_args=['-std=c++17'],
        language = "c++"),

        Extension("ops", 
        ["ops.pyx"], 
        libraries=["fst", "fstfar", "fstscript", "fstfarscript"],
        extra_compile_args=['-std=c++17'],
        language = "c++")
    ])
)
