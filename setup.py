import setuptools
setuptools.setup(
    include_package_data=True,
    name='epam-flask',
    version='0.0.1',
    description='Flask project for EPAM',
    url='https://github.com/DmytroY/EPAM-Flask',
    author='Dmytro Yakovenko',
    author_email='dmitry.yakovenko@gmail.com'
    packages=setuptools.find_packages(),
    install_requirements=[],
    long_description='Flask project for EPAM',
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Lamguage :: Python3",
        "Operating System :: Ubuntu",
    ]

)