from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    # 2.x
    from distutils.command.build_py import build_py

setup(name="BeautifulSoup4",
    version="4.0b3",
    author="Leonard Richardson",
    url="http://www.crummy.com/software/BeautifulSoup/",
    packages=['bs4', 'bs4.builder', 'bs4.tests'],
    cmdclass = {'build_py':build_py},
    classifiers=[
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
    ],
)
