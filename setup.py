#!/usr/bin/env python
from setuptools import setup

version = "0.1.0"
setup(name='Regex-Dict',
      version=version,
      description='A dict with sugar for regex searching over string keys.',
      author='CJ Carey',
      author_email='perimosocordiae@gmail.com',
      url='http://github.com/perimosocordiae/regexdict',
      license='MIT',
      classifiers=[
          'Development Status :: 4 - Beta',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
      ],
      packages=['regexdict'],
      test_suite='test'
      )
