# Micropeutist API documentation

## 1. Overview
Micropeutist API is RESTful JSON-based API. All requests are made to endpoint begining   **.../api/**.
All request must be secure, i.e. **https**, not **http**.

In the examples below all requests has *Host: 127.0.0.1:5000* which is related to the test development server. Note that in live version proper host shoud be used.


## 2. API for Doctor records

### 2.1. Retrieving List of doctors

**Routes:** /api/ ,  /api/doctors/

**Method:** GET

**Passed parameters:** None

**Response** on success should include status code 200 and list of doctors with next field for each of doctor:
- id,
- first_name,
- last_name,
- grade,
- specialization,
- email,
- patient_count.

**Request example**
```
GET http://127.0.0.1:5000/api/doctors/
---------
GET /api/doctors/ HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
```
**Response example**
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 423
Connection: close
 
[
{
"email": "jh_watson@micropeutist.com",
"first_name": "Jonh",
"grade": "BM",
"id": 4,
"last_name": "Watson",
"patient_count": 3,
"specialization": "Combat medic"
},
{
"email": "w@w.w",
"first_name": "Updated_name",
"grade": "GRADE",
"id": 11,
"last_name": "Updated_name2",
"patient_count": 0,
"specialization": "Updated_specialization"
}
]
```
  

### 2.2. Creating doctor record

**Route:** /api/create_doctor

**Method:** POST

**Passed parameters:**

| Parameter | Type | Required? | comment| 
|---|---|---|---|
|first_name    |string|required|   |
|last_name     |string|required|   |
|grade         |string|optional|doctors educational grade: MD, MS, BM, other...  |
|specialization|string|optional|Doctor specialization, for example "Terapeutist" |
|email         |string|required|Unique. Can be used as key in CRUD operations if **id** field does not provided    |


**Response**: 
On success: Sucsess message and status code 201. 
On error: Error description adnd status code 409.

Record with duplicated email should not be created, system should return an error.

**Request example**
```
POST /api/create_doctor HTTP/1.1
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
Content-Length: 135
Referer: http://127.0.0.1:5000/api/create_doctor
Host: 127.0.0.1:5000
 
{
"first_name":"John",
"last_name":"Wolf",
"grade":"MD",
"specialization":"Terapeutist",
"email":"wolf@email.com"
}
```
**Response example**
```
HTTP/1.1 201 CREATED
Content-Type: application/json
Content-Length: 47
Connection: close
 
{
"message": "Doctor Wolf have been added"
}
```
**Response example in case of record can not be created**
```
HTTP/1.1 409 CONFLICT
Content-Type: application/json
Content-Length: 69
Connection: close
 
{
"message": "Error. This email already exist in Doctor records"
}
```

### 2.3. Receiving doctor record information

**Route:** /api/receive_doctor

**Method:** GET.

**Passed parameters:** Either *id* or *email*.

**Response** on success should include status code 200 and next data:
- id,
- first_name,
- last_name,
- grade,
- specialization,
- email,
- related patients info:
  - id, 
  - first_name,
  - last_name,
  - gender,
  - health_state,
  - birthday date,
  - age,
  - email.

On error: status code 204 and error message

**Request example**
```
GET /api/receive_doctor/?id=6 HTTP/1.1
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate, br
```
**Response example**
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 501
Connection: close
 
{
"email": "house_md@micropeutist.com",
"first_name": "Gregory",
"grade": "MD",
"id": 6,
"image_url": "/static/photo/house_md_micropeutist_com.jpg",
"last_name": "House",
"patients": [
{
"age": 16,
"birthday": "2006-05-03",
"doctor_id": 6,
"email": "rat@steve.mc",
"first_name": "Steve",
"gender": "male",
"health_state": "under diagnosis process",
"id": 4,
"last_name": "McQueen"
}
],
"specialization": "Nephrologist"
}
```
**Response in case of trying get not existed record**
```
HTTP/1.1 204 NO CONTENT
Content-Type: text/html; charset=utf-8
Connection: close
```


### 2.4. Updating doctor record information

**Route:** /api/update_doctor

**Method:** PUT.

**Passed parameters:**

| Parameter | Type | Required?| comment| 
|---|---|---|---|
|id            |int|semi-required*|Either **id** or **email** should be provided to identify record
|first_name    |string|optional|   |
|last_name     |string|optional|   |
|grade         |string|optional|doctors educational grade: MD, MS, BM, other...  |
|specialization|string|optional|Doctor specialization, for example "Terapeutist" |
|email         |string|semi-required*|Either **id** or **email** should be provided to identify record   |

*- in case of **id** parameter missed record will be identificated by **email**

**Response** on success should include status code 201 and message, 
on error: status code 409 and error message.

**Request example**
```
PUT /api/update_doctor HTTP/1.1
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
Content-Length: 128
Referer: http://127.0.0.1:5000/api/update_doctor
Host: 127.0.0.1:5000
 
{
"email": "house_md@micropeutist.com",
"first_name": "Greg",
"grade": "MD",
"id": 6,
"last_name": "House"
}
```
**Response example**
``` 
HTTP/1.1 201 CREATED
Content-Type: application/json
Content-Length: 50
Connection: close
 
{
"message": "Doctor House have been updated"
}
```
**Response in case of trying update not existed record**
``` 
HTTP/1.1 409 CONFLICT
Content-Type: application/json
Content-Length: 50
Connection: close
 
{
"message": "Error. No record with such key"
}

```


### 2.5. Deleting doctor record

**Route:** /api/delete_doctor

**Method:** DELETE

**Passed parameters:**  Either *id* or *email*
| Parameter | Type | Required?| comment| 
|---|---|---|---|
|id |int/string|required|Both **id** or **email** can be used here

**Response**. 
On success: sucsess message and status code 200. 
On error: error description and status code 409.

**Request example**
```
DELETE /api/delete_doctor HTTP/1.1
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
Content-Length: 30
Referer: http://127.0.0.1:5000/api/delete_doctor
Host: 127.0.0.1:5000
 
{
"id": "wolf@email.com"
}
```
**Response example**
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 75
Connection: close
 
{
"message": "Doctor with id/email = wolf@email.com have been deleted"
}
```

**Response if we try delete not existed record**
```
HTTP/1.1 409 CONFLICT
Content-Type: application/json
Content-Length: 57
Connection: close
 
{
"message": "No such doctor record in the database"
}
```

==============================


## 3. API for Patient records

### 3.1. Retrieving whole list of patients

**Route:**/api/patients/

**Method:** GET

**Passed parameters:** None

**Response** on success should include status code 200 and list of patients with next field for each of patient:
- id,
- first_name,
- last_name,
- gender,
- health_state,
- birthday,
- age,
- email,
- related doctor id.
- related doctor datails:
  - id
  - first_name
  - last_name
  - grade
  - specialization
  - email

**Request example**
```
GET /api/patients/ HTTP/1.1
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate, br
```
**Response example**
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 442
Connection: close
 
[
{
"age": 205,
"birthday": "1818-01-01",
"doctor": {
    "email": "frankenstein@victor.com",
    "first_name": "Victor",
    "grade": "",
    "id": 7,
    "last_name": "Frankenstein",
    "specialization": "Patalogist"
    },
"doctor_id": 7,
"email": "creature@death.io",
"first_name": "Creature",
"gender": "male",
"health_state": "either alive or dead",
"id": 3,
"last_name": "Victorson"
},
{
"age": 16,
"birthday": "2006-05-03",
"doctor": {
    "email": "house_md@micropeutist.com",
    "first_name": "Greg",
    "grade": "MD",
    "id": 6,
    "last_name": "House",
    "specialization": null
    },
"doctor_id": 6,
"email": "rat@steve.mc",
"first_name": "Steve",
"gender": "male",
"health_state": "under diagnosis process",
"id": 4,
"last_name": "McQueen"
}
]

```

### 3.2. Retrieving filtered list of patients

**Route:**/api/patients/

**Method:** POST

**Passed parameters:**
| Parameter | Type | Required?| comment| 
|---|---|---|---|
|birthday_since|date|optional*|first date for filter. Format "YYYY-MM-DD"|
|birthday_till |date|optional*|last date for filter. Format "YYYY-MM-DD"|
|doctor_id     |int |optional*|id of doctor record|

*-In case of no paramenters provided response will contain whole list of patients

**Response** on success should include status code 200 and list of patients which satisfied passed parameters creterias. Response should contain same fieds as in pargraph *2.2.1. Retrieving whole list of patients*.

**Request example**
```
OST /api/patients/ HTTP/1.1
Content-Type: application/json
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate, br
Content-Length: 95
 
{
"birthday_since": "2005-11-16",
"birthday_till": "2005-11-16",
"doctor_id": "4"
}
```
**Response example**
```
 
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 430
Connection: close
 
[
{
"age": 17,
"birthday": "2005-11-16",
"doctor": {
    "email": "jh_watson@micropeutist.com",
    "first_name": "Jonh",
    "grade": "BM",
    "id": 4,
    "last_name": "Watson",
    "specialization": "Combat medic"
    },
"doctor_id": 4,
"email": "laura@email.com",
"first_name": "Laura",
"gender": "female",
"health_state": "healthy",
"id": 6,
"last_name": "Capway"
}
]

```

  

### 3.3. Creating patient record

**Routes:** /api/create_patient

**Method:** POST

**Passed parameters:**
| Parameter | Type | Required?| comment| 
|---|---|---|---|
|first_name  |string|required|    |
|first_name  |string|required|    |
|gender      |string|required| either "male" or "female"|
|health_state|string|optional|    |
|birthday    |date  |required|Format "YYYY-MM-DD"|
|email       |string|required|Unique|
|doctor_id   |int   |optional|id of related doctor|

**Response**: 
On success: Sucsess message and status code 201. 
On error: Error description adnd status code 409.

Record with duplicated email should not be created, system should return an error.

**Request example**
```
POST /api/create_patient HTTP/1.1
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 181
Referer: http://127.0.0.1:5000/api/create_patient
Host: 127.0.0.1:5000
 
{
"first_name": "Hanna",
"last_name": "Lou",
"gender": "female",
"health_state": "unknown health state",
"email": "hanna@lou.com",
"birthday": "2000-04-21"
}
```
**Response example**
```
HTTP/1.1 201 CREATED
Server: Werkzeug/2.2.2 Python/3.10.6
Date: Sun, 05 Mar 2023 18:43:25 GMT
Content-Type: application/json
Content-Length: 47
Connection: close
 
{
"message": "Patient Lou have been added"
}
```

### 3.4. Receiving patient record information

**Routes:** /api/receive_patient

**Method:** GET.

**Passed parameters:** Either *id* or *email*.

**Response** on success should include status code 200 and next data:
- id,
- first_name,
- last_name,
- gender,
- health_state,
- birthday,
- age,
- email,
- related doctor id.

On error: status code 204 and error message.

**Request example**
```
GET /api/receive_patient?id=laura@email.com HTTP/1.1
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Referer: http://127.0.0.1:5000/api/receive_patient?id=laura@email.com
Host: 127.0.0.1:5000
```
**Response example**
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.2 Python/3.10.6
Date: Sun, 05 Mar 2023 18:50:19 GMT
Content-Type: application/json
Content-Length: 427
Connection: close
 
{
"birthday": "2005-11-16",
"doctor": {
    "email": "jh_watson@micropeutist.com",
    "first_name": "Jonh",
    "grade": "BM",
    "id": 4,
    "last_name": "Watson",
    "specialization": "Combat medic"
    },
"doctor_id": 4,
"email": "laura@email.com",
"first_name": "Laura",
"gender": "female",
"health_state": "healthy",
"id": 6,
"image_url": "/static/photo/laura_email_com.jpg",
"last_name": "Capway"
}
```
**Response in case of trying get not existed record**
```
HTTP/1.1 204 NO CONTENT
Content-Type: text/html; charset=utf-8
Connection: close
```

### 3.5. Updating patient record information

**Routes:** /api/update_patient

**Method:** PUT.

**Passed parameters:**
| Parameter | Type | Required?| comment| 
|---|---|---|---|
|id          |int   |semi-required*|either **id** or **email** should be provided to identify record|
|first_name  |string|optional|    |
|first_name  |string|optional|    |
|gender      |string|optional| either "male" or "female"|
|health_state|string|optional|    |
|birthday    |date  |optional|Format "YYYY-MM-DD"|
|email       |string|semi-required*|either **id** or **email** should be provided to identify record|
|doctor_id   |int   |optional|id of related doctor|

*- in case of **id** parameter missed record will be identificated by **email**


**Response** on success should include status code 201 and message, 
on error: status code 409 and error message.

**Request example**
```
PUT /api/update_patient HTTP/1.1
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 178
Referer: http://127.0.0.1:5000/api/update_patient
Host: 127.0.0.1:5000
 
{
"first_name": "Louis",
"last_name": "Bang",
"gender": "male",
"health_state": "healty",
"email": "w@w.w",
"birthday": "1999-11-25",
"doctor_id": 4
}
```
**Response example**
```
HTTP/1.1 201 CREATED
Content-Type: application/json
Content-Length: 50
Connection: close
 
{
"message": "Patient Bang have been updated"
}
```
**Response example in case of trying update not existing record**
```
TTP/1.1 409 CONFLICT
Content-Type: application/json
Content-Length: 50
Connection: close
 
{
"message": "Error. No record with such key"
}
```


### 3.6. Deleting patient record

**Routes:** /api/delete_patient

**Method:** DELETE

**Passed parameters:**  Either *id* or *email*
| Parameter | Type | Required?| comment| 
|---|---|---|---|
|id |int/string|required|Both **id** or **email** can be used here

**Response**. 
On success: sucsess message and status code 200. 
On error: error description and status code 409.

**Request example**
```
DELETE /api/delete_patient HTTP/1.1
Content-Type: application/json
Accept-Encoding: gzip, deflate, br
Content-Length: 21
Referer: http://127.0.0.1:5000/api/delete_patient
Host: 127.0.0.1:5000
 
{
"id": "w@w.w"
}
```
**Response example**
```
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 67
Connection: close
 
{
"message": "PAtient with id/email = w@w.w have been deleted"
}
```
**Response in case we try to delete not existing record**
```
HTTP/1.1 409 CONFLICT
Content-Type: application/json
Content-Length: 58
Connection: close
 
{
"message": "No such patient record in the database"
}

```
