import os
from setuptools import setup
 
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
 
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name='sebam2k4_reusable_blog',
    version='1.0.0',
    packages=['sebam2k4_reusable_blog'],
    include_package_data=True,
    license='BSD License',
    description='A simple reusable blog for Django projects',
    long_description=README,
    url='https://github.com/sebam2k4/sebam2k4_reusable_blog',
    author='Sebastian Kulig',
    author_email='sebam2k4@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        'pillow',
        'django-disqus',
    ],
)