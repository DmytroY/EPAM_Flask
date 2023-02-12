# Micropeutist

## Vision

"Micropeutist" is web-application which allows manage information about district doctors and attached to them patients.

The application should provide:
- Storing data about new patients and doctors in a database;
- Display list of doctors;
- Update list of doctors (add, edit, delete);
- Display list of patients;
- Update list of patients (add, edit, delete);
- Display list of patients for each doctor;
- Filtering for patients by age, gender, doctor;

## 1. Doctors
### 1.1. Display list of doctors
*Main scenario:*

As User select "Doctors" menu tab, the application display list of doctors.

---
![Doctors_List](/documentation/mockups/Doctor-list.svg)
---

**The page contains:**
#### 1) Menu with tabs
- Doctors (accented, inactive)
- Patients

#### 2) List of doctors
- Name
- Grade
- Specialisation
- Count of curently supervised patients

#### 3) Button for adding new doctor

**Possible actions:**
- click on "Patients" tab in menu to see full list of patients;
- click on doctor's name to jump to specitic doctor page to see more details and edit or delete the doctor record;
- push "ADD" button to open doctor creating form.


### 1.2. Display the doctor
*Main scenario:*

User click on the doctor's name in the list of doctors the application jump to the doctor's detail view page.

---
![Doctor](/documentation/mockups/Doctor.svg)
---

**The page contains:**
#### 1) Menu with tabs
- Doctors
- Patients
#### 2) A table with the Doctor's information
- First Name
- Last Name
- Grade
- Specialization
- email

#### 3) Buttons
- EDIT the doctors info
- DELETE the doctor

#### 4) List of patients curently supervised by the doctor
- Patient Name
- Age
- Gender
- State of health

#### 5) Button to add a patient

**Possible actions:**
- click on "Doctor" or "Patients" tab in menu to see full list of doctors or patients respectively;
- push "EDIT" button to change information about the doctor;
- push "DELETE" button to delete the doctor;
- click on patient's name to jump to specitic patient page to see more details and edit or delete the patient record;
- push "ADD" button to create a patient linked to this doctor

### 1.3. ADD or EDIT the doctor
*Main scenario:*

User either push "ADD" button on the page with list of doctors
or "EDIT" button on the particular doctor's page, the application jump to the doctor creation/edit form.

---
![Doctor_edit](/documentation/mockups/Add-Edit-Doctor.svg)
---

**The page contains:**
#### 1) Menu with tabs
- Doctors
- Patients
#### 2) A table for the Doctor's information. Table fields either contains actual information in case of editing, or are empty in case of creating new doctor
- First Name
- Last Name
- Grade
- Specialization
- email

#### 3) Buttons
- SAVE

**Possible actions:**
- click on "Doctor" or "Patients" tab in menu to see full list of doctors or patients respectively;
- edit fields for imput;
- push "SAVE" button to save the doctor's info;


## 2. Patients
### 2.1. Display list of Patients
*Main scenario:*

As User select "Patients" menu tab, the application display list of patients.

---
![Patient_List](/documentation/mockups/Patient-list.svg)
---

**The page contains:**
#### 1) Menu with tabs
- Doctors 
- Patients (accented, inactive)
#### 2) Search block with next elements
- "Doctor" filter drop-down list field
- "SEARCH" Button
#### 3) List of Patients
- Name
- Age
- Gender
- State
- Related doctor

**Possible actions:**
- click on "Doctors" tab in menu to see full list of doctors;
- fill search form fields and click "SEARCH" button to change list of patients according to search criterias;
- click on patient's name to jump to specitic patient page to see more details and edit or delete the patient's record;
- click on doctor's name to jump to specitic doctor page to see more details and edit or delete the doctor record.


### 2.2. Display the patient
*Main scenario:*

User click on the patients's name in the list of patients the application jump to the patients's detail view page.

---
![Patient](/documentation/mockups/Patient.svg)
---

**The page contains:**
#### 1) Menu with tabs
- Doctors
- Patients
#### 2) A table with the patient's information
- First Name
- Last Name
- Gender
- Birthday
- State of health
- email
- Doctor

#### 3) Buttons
- EDIT the patients info
- DELETE the patient

**Possible actions:**
- click on "Doctor" or "Patients" tab in menu to see full list of doctors or patients respectively;
- push "EDIT" button to change information about the patient;
- push "DELETE" button to delete the patient;
- click on doctors's name to jump to specitic doctor page to see more details and edit or delete the doctor record;


### 2.3. ADD or EDIT the patient
*Main scenario:*

User either push "ADD" button on the doctor's page with list of patient
or "EDIT" button on the particular patients's page, the application jump to the patient creation/edit page.

---
![Patient_Edit](/documentation/mockups/Add-Edit-Patient.svg)
---

**The page contains:**
#### 1) Menu with tabs
- Doctors
- Patients
#### 2) A table for the Patient's information. Table fields either contains actual information in case of editing, or are empty in case of creating new patient
- First Name
- Last Name
- Gender
- Year of birth
- State of health
- email
- Doctor

#### 3) Buttons
- SAVE

**Possible actions:**
- click on "Doctor" or "Patients" tab in menu to see full list of doctors or patients respectively;
- edit fields for imput;
- push "SAVE" button to save the patients's info.
