"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='plotly_flask_tutorial',
    version='0.0.1',
    description='Tutorial for embedding a Plotly Dash app inside a Flask app.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/toddbirchard/plotlydash-flask-tutorial',
    author='Todd Birchard',
    author_email='toddbirchard@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='Plotly Dash Flask',
    packages=find_packages(),
    install_requires=['flask',
                      'flask_assets',
                      'pandas',
                      'dash',
                      'dash_core_components',
                      'dash_html_components',
                      'dash_table',
                      'dash_renderer',
                      'pathlib'],
    entry_points={
        'console_scripts': [
            'run = wsgi:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/toddbirchard/plotlydash-flask-tutorial/issues',
        'Source': 'https://github.com/toddbirchard/plotlydash-flask-tutorial/',
    },
)
