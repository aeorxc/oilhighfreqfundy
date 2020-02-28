from setuptools import setup
import os

# Major and minor versions
majorVersion = 1
minorVersion = 1


# Get build number
def __path(filename):
    return os.path.join(os.path.dirname(__file__), filename)


build = 0
if os.path.exists(__path('build.info')):
    build = open(__path('build.info')).read().strip()

versionStr = '{0}.{1}.{2}'.format(majorVersion, minorVersion, build)

setup(
    name='oilhighfreqfundy',
    version=versionStr,
    packages=['oilhighfreqfundy'],
    test_suite='tests',
    url='',
    license='MIT',
    author='aeorxc',
    author_email='',
    description='Fetch high frequency oil data from likes of EIA, PJK, PAJ',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3.5'
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
