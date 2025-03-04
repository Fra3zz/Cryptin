from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Simple crypto operations'
LONG_DESCRIPTION = "Simple crypto package of things that I don' see in other common cryptography modules"

# Setting up
setup(
        name="Cryptin", 
        version=VERSION,
        author="Fra3zz",
        author_email="",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["asn1tools", "pyasn1"], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        package_data={'Cryptin': ['crypt/timestamp/tsp.asn']},

        keywords=['python', 'cryptography', "crypto"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Cryptography",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)