import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
  name='fython',
  version='0.0.4',
  license='MIT',
  packages=['fython'],
  description='Functional utilities for Python, inspired by Scala',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author='Tsah Weiss',
  url='https://github.com/tsah/fython',
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
