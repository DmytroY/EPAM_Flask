# EPAM-Flask

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Build Status](https://app.travis-ci.com/DmytroY/EPAM_Flask.svg?branch=main)](https://app.travis-ci.com/DmytroY/EPAM_Flask)
[![Coverage Status](https://coveralls.io/repos/github/DmytroY/EPAM_Flask/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/DmytroY/EPAM_Flask?branch=main)


## What is it? 
It is final project of EPAM Python spring program 2022 course.

It supposed to demonstrate skills and knowleges acquired by the student. Mainly focused of back-end development process.

## Main technologies used in the project:
- Flask framework
- MySQL database
- SQLALchemy ORM
- Alembic migration tool

## Project folders structure:
- **documentation** folder which includes:
  - SRS, 
  - API specification,
  - html_prototypes.
- **micropeutist_app** folder which includes flask application and all required modules
- **tests** folder which includes unit-tests

## Install and run

0. Prerequisites. Instalation process describeb for Ubuntu linux, for other operational system comands may vary but steps and idea are the same. You should have MySQL, git, python3 and pip installed. By default to access MySQL database application use user *root* and blank password.

1. Create folder where you wish to install application and go to this folder
```
> mkdir mydir
> cd mydir
```

2. Install virtual environment
```
mydir> python3 -m venv venv
```

3. Activate virtual environment. The **venv/bin/** folder contains several script for different shells and OS. Actual script depend on which shell you use. In case of bash do:
```
mydir> source venv/bin/activate
(venv)>
```
(venv) prefix indicates that virtual environment activated. You can always leave virtual environment with comand "deactivate".

4. Clone github repository
```
(venv)mydir> git clone https://github.com/DmytroY/EPAM_Flask.git
```

5. Go to the cloned folder EPAM_Flask
```
(.venv)mydir> cd EPAM_Flask
``` 
 
6. Install dependensies
```
(.venv)mydir/EPAM_Flask> pip install -r requirements.txt
```
REMARK: This step can be interrupted with Deprecate setup.py install fallback, see details here https://github.com/pypa/pip/issues/8559. --use-pep517 flag can help in this case:
```
(.venv)mydir/EPAM_Flask> pip install -r requirements.txt --use-pep517
```

7. Configure database.
Either in MySQL workbench or by CLI create database with name micropeutist
```
> mysql -u root -p -e 'CREATE DATABASE micropeutist'
```
When you are in folder EPAM_Flask, apply migrations to create tables which correspond python ORM objects
```
(venv)mydir/EPAM_Flask> flask db upgrade
```

8. Runing.

When you are in folder EPAM_Flask, you can start flask development server with "flask run" command :
```
(venv)mydir/EPAM_Flask> flask run                      
 * Serving Flask app 'main.py'
 * Debug mode: on
[2023-03-06 19:40:30,882] INFO. modul _internal, function _log: WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
[2023-03-06 19:40:30,883] INFO. modul _internal, function _log: Press CTRL+C to quit
```

Web application will be available at address http://127.0.0.1:5000/

API will be available at address http://127.0.0.1:5000/API/



Alternatively you can launch production gunicorn server:
```
(venv)mydir/EPAM_Flask> gunicorn main:app
```
By default web application will be available at address http://127.0.0.1:8000/
API will be available at address http://127.0.0.1:8000/API/


Please see detailed API specification in **documentation** folder.