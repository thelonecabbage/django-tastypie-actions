import os
from setuptools import setup
import tastypie_actions

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
VERSION = tastypie_actions.__version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-tastypie-actions',
    version=VERSION,
    packages=['tastypie_actions'],
    include_package_data=True,
    install_requires=['django-tastypie'],
    license='GPLv2',
    description='Adds the ability to (easily) append actions to Tastypie resources.',
    long_description=README,
    url='https://github.com/thelonecabbage/django-tastypie-actions',
    author='Justin Alexander',
    author_email='',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
