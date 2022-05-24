import setuptools
from setuptools import setup

# with open("README.md", 'r') as f:
#     long_description = f.read()

setup(
   name='Watermarkd',
   version='0.7.1.2',
   description='A friendly watermarking tool with optional GUI component.',
   license="Apache-2.0",
#    long_description=long_description,
   long_description_content_type="text/markdown",
   author='holypython.com',
   author_email='watermarkd@holypython.com',
   url="https://holypython.com/",
   download_url = 'https://github.com/holypython/Watermarkd/archive/0.7.1.2.tar.gz',
   packages=['Watermarkd'],
   keywords = ['watermarking', 'image processing', 'watermark', 'photography', 'copyrights', 'holypython', 'batch watermark', 'holypython.com'],
   classifiers=[
       "Development Status :: 3 - Alpha",
       "Intended Audience :: Developers",
       "Intended Audience :: Education",
       "Intended Audience :: End Users/Desktop",
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: Apache Software License",
       "Operating System :: OS Independent",
   ],

   install_requires=[
       'pillow',
       'pysimplegui',
   ],

   python_requires='>=3.6'
)