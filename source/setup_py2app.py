"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['monorail.py']
DATA_FILES = ['error_mm.log', 'quest.stat']
OPTIONS = {'argv_emulation': True,
 'iconfile': '/Users/koenwitters/monorail/source/icon.icns'}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
