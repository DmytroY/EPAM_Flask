# EPAM-Flask micropeutist application

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
- **micropeutist** folder which includes flask application and all required modules
- **tests** folder which includes unit-tests

## Install and run

### 0. Prerequisites.
Instalation process describeb for Ubuntu linux, for other operational system comands may vary but steps and idea are the same. You should have already been installed:
 * MySQL,
 * git,
 * python3,
 * pip,
 * setuptools,
 * bild,
 * gunicorn.
 
 By default to access MySQL database application use user *root* and blank password.

### 1. Create folder where you wish to install application and go to this folder
```
> mkdir mydir
> cd mydir
```

### 2. Install virtual environment
for linux:
```
mydir> python3 -m venv venv
```
for Windows:
```
mydir> py -m venv venv
```

### 3. Activate virtual environment.
The **venv/bin/** folder contains several script for different shells and OS. Actual script depend on which shell you use. 

For Linux Bash do:
```
mydir> source venv/bin/activate
(venv)mydir>
```
fo Windows PowerShell:
```
mydir> .venv/bin/activate.ps1
(.venv)mydir>
```

(venv) prefix indicates that virtual environment activated. You can always leave virtual environment with comand "deactivate".

### 4. Install from github
```
(venv)mydir> pip install git+https://github.com/DmytroY/EPAM_Flask.git
```
now micropeutist module is available in pip installed modules, you can check it with **pip list**:
```
(venv)mydir> pip list | grep "micropeutist"
micropeutist      1.0.1
(venv)mydir>
```

### 5. Configure database.
Either in MySQL workbench or by CLI create database with name **micropeutist**. It you want do it via Bash use next command:
```
> mysql -u root -p -e 'CREATE DATABASE micropeutist'
```
Initiate, create and apply migrations to create tables which correspond python ORM objects
```
(venv)mydir> flask micropeutist.application db init
(venv)mydir> flask micropeutist.application db migrate
(venv)mydir> flask micropeutist.application db upgrade
(venv)mydir>
```
check that tables are created in database:
```
> mysql -u root -p -e 'USE micropeutist; SHOW TABLES;'
Enter password:
+------------------------+
| Tables_in_micropeutist |
+------------------------+
| alembic_version        |
| doctors                |
| patients               |
+------------------------+
```
Congratulations! 
Installation finished.
### 6. Runing production server:
```
(venv)mydir> gunicorn micropeutist.application:app
```
By default web application will be available at address http://127.0.0.1:8000/
API will be available at address http://127.0.0.1:8000/API/

Also you can run the appliation with Flask development server:
```
(venv)mydir>flask --app micropeutist.application run
```
In this case web application will be available at address http://127.0.0.1:5000/
API will be available at address http://127.0.0.1:5000/API/

---------------------------
Please see detailed API specification in **documentation** folder.
