from setuptools import setup, find_packages, Extension
import pybind11
import os

def readme():
  with open(os.path.join(os.getcwd(),"README.md"), 'r') as f:
    return f.read()

ext_modules = [
    Extension(
        "console_tool",
        ["tpg/console_tool.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++"
    )
]


setup(
  name='tpg',
  version='1.5.3',
  author='@HITHELL',
  author_email='hit<@HITHELL.com>',
  description="легкая библиотека для работы с псевдо графикой в терминале",
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/xHak2215/tpg',
  packages=find_packages(),
  install_requires=['keyboard>=2.25.1','psutil==7.1.3','subprocess'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: MIT License',
    'Operating System :: Windows'
  ],
  keywords='tpg/tpg.py',
  project_urls={
    'GitHub': 'https://github.com/xHak2215/tpg'
  },
  python_requires='>=3.12',
  ext_modules=ext_modules
)
