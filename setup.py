import sys

from Cython.Build import cythonize
from setuptools import Extension, setup

sys.path.append('fstlib/cext')

setup(
    name='FSTlib',
    version='0.1',
    author='Roland F Schwarz',
    author_email='roland.f.schwarz@gmail.com',
    description='Minimum Event Distance for Intra-tumour Copy-number Comparisons',
    long_description=open('README.MD').read(),    
    url='https://bitbucket.org/schwarzlab/fstlib',
    classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
    ],
    packages=['fstlib', 'fstlib.cext'],
    license='GPL-3',
    ext_modules = cythonize([
        Extension("fstlib.cext.pywrapfst", 
                  ["fstlib/cext/pywrapfst.pyx"],
                  include_dirs=['fstlib/cext'],
                  libraries=["fst", "fstfar", "fstscript", "fstfarscript"],
                  extra_compile_args=['-std=c++17'],
                  language = "c++"),

        Extension("fstlib.cext.ops", 
                  ["fstlib/cext/ops.pyx"],
                  include_dirs=['fstlib/cext'],
                  libraries=["fst", "fstfar", "fstscript", "fstfarscript"],
                  extra_compile_args=['-std=c++17'],
                  language = "c++")
    ])
)
