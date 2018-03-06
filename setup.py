import os.path
import codecs
from setuptools import setup, find_packages

long_description = None

if os.path.exists('README.md'):
    with codecs.open('README.md', 'r', 'utf-8') as f:
        long_description = f.read()
        try:
            import pandoc
            pandoc.core.PANDOC_PATH = '/usr/local/bin/pandoc'
            doc = pandoc.Document()
            doc.markdown = long_description
            long_description = doc.rst
        except ImportError:
            pass

setup(
    name = 'django-markdown2',
    version = '0.3.1',
    description = 'This is a simple app, which supplies a single template tag for markdown markup.',
    long_description = long_description,
    keywords = 'django apps utils',
    license = 'New BSD License',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    url = 'http://github.com/svetlyak40wt/django-markdown2/',
    install_requires = ['markdown2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
    include_package_data = True,
)
