# python setup.py sdist
# tar --list -f dist/micropeutist-1.0.tar.gz

def parse_reqs(filename: str) -> list:
    ''' parse requirements file to list'''
    result = []
    with filename.open() as file:
        for line in file:
            result.append(line[:-1:])
    return result

import setuptools
setuptools.setup(
    name='micropeutist',
    version='1.0',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=parse_reqs("requirements.txt")
    )