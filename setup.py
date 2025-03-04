from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Simple xor operation'
LONG_DESCRIPTION = 'Simple xor opeartions with the creation of xor object.'

# Setting up
setup(
        name="Cryptin", 
        version=VERSION,
        author="Fra3zz",
        author_email="",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'xor'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Cryptography",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)