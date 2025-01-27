# EPAM-Flask micropeutist application

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)
[![Build Status](https://app.travis-ci.com/DmytroY/EPAM_Flask.svg?branch=main)](https://app.travis-ci.com/DmytroY/EPAM_Flask)
[![Coverage Status](https://coveralls.io/repos/github/DmytroY/EPAM_Flask/badge.svg?branch=main&kill_cache=1)](https://coveralls.io/github/DmytroY/EPAM_Flask?branch=main)


## What is it? 
It is simple cusomer management database with simple 2 level "one to many" structure (doctor - patients).
Whole spector of CRUD operations covered by WEB and API interfaces.

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
- **micropeutist** folder which includes Flask application and all required modules
- **tests** folder which includes unit-tests

## Install and run

### 0. Prerequisites.
Instalation process is described mainly for Linux, for other operational systems commands may vary but the steps and ideas are the same. You should have already installed:
 * MySQL,
 * git,
 * python3,
 * pip,
 * setuptools,
 * bild,
 * gunicorn.
 

### 1. Create a folder where you wish to install the application and go to this folder
```
> mkdir mydir
> cd mydir
```

### 2. Install virtual environment
for Linux:
```
mydir> python3 -m venv venv
```
for Windows:
```
mydir> py -m venv venv
```

### 3. Activate virtual environment.
The **venv/bin/** folder contains several scripts for different shells and OS. The actual script depends on which shell you use. 

For Linux Bash do:
```
mydir> source venv/bin/activate
(venv)mydir>
```
for Windows PowerShell:
```
mydir> venv\Scripts\Activate.ps1
(venv)mydir>
```

(venv) prefix indicates that virtual environment is activated. You can always leave virtual environment with the command "deactivate".

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
For access to MySQL database micropeutist application will use password and login. The application will get it from environment variables DB_USER and DB_PASS respectively. So initialize those variables.

Linux Bash:
```
(venv)mydir> export DB_USER="<put your MySQL user here>"
(venv)mydir> export DB_PASS="<put your MySQL password here>"
```
Windows Powershell:
```
(venv)mydir> $env:DB_USER = "<put your MySQL user here>"
(venv)mydir> $env:DB_PASS = "<put your MySQL password here>"
```
If for some reason you use access to the database without a password (empty password) just omit to create DB_PASS environment variable.

Also, you should create a database that will be used by the application. Either in MySQL workbench or by CLI create a database with the name **micropeutist**. If you want to do it via Bash use the next command:
```
> mysql -u root -p -e 'CREATE DATABASE micropeutist'
```
Then initiate, create, and apply migrations to create tables that correspond to python ORM objects:
```
(venv)mydir> flask micropeutist.application db init
(venv)mydir> flask micropeutist.application db migrate
(venv)mydir> flask micropeutist.application db upgrade
(venv)mydir>
```
check that tables are created in the database:
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
Installation is finished.
### 6. Running production server:
```
(venv)mydir> gunicorn micropeutist.application:app
```
By default, the web application will be available at the address http://127.0.0.1:8000/ .
API will be available at the address http://127.0.0.1:8000/API/

Also, you can run the application with Flask development server:
```
(venv)mydir>flask --app micropeutist.application run
```
In this case, web application will be available at the address http://127.0.0.1:5000/ .
API will be available at the address http://127.0.0.1:5000/API/


---------------------------
Detailed API specifications you can find in **documentation** folder.
