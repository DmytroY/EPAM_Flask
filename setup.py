# import setuptools
# setuptools.setup(
#     include_package_data=True,
#     name='epam-flask',
#     version='0.0.1',
#     description='Flask project for EPAM',
#     url='https://github.com/DmytroY/EPAM-Flask',
#     author='Dmytro Yakovenko',
#     #author_email='dmitry.yakovenko@gmail.com'
#     packages=setuptools.find_packages(),
#     install_requirements=[],
#     long_description='Flask project for EPAM',
#     long_description_content_type='text/markdown',
#     classifiers=[
#         "Programming Lamguage :: Python3",
#         "Operating System :: Ubuntu",
#     ]

# )

import setuptools
setuptools.setup(
    name='Micropeutist',
    version='1.0',
    long_description=__doc__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['alembic==1.9.4','Flask==2.2.3', 'Flask_Migrate==4.0.4', 'flask_sqlalchemy==3.0.3', 'SQLAlchemy==2.0.3']
)