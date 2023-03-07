from micropeutist.application import app


class TestHomeRoute():
    ''' Testing home route'''
    def test_route_home(self):
        responce = app.test_client().get('/')
        assert responce.status_code == 200
        assert b'List of Doctors' in responce.data

class TestDoctorCRUD():
    ''' Testing routes for doctors'''
    test_data = dict(first_name='Pedro', last_name='Sanches', grade='TG', specialization='ts', email='test@email.com')
    
    # delete record with test data if exist
    app.test_client().delete('/api/delete_doctor/', json={'id': test_data['email']})

    def test_route_doctors(self):
        responce = app.test_client().get('/doctors/')
        assert responce.status_code == 200
        assert b'List of Doctors' in responce.data

    def test_route_new_doctor_get(self):
        responce = app.test_client().get('/new_doctor/')
        assert responce.status_code == 200
        assert b'Creating new doctor record' in responce.data

    def test_route_new_doctor_post(self):
        responce = app.test_client().post('/new_doctor/', data=self.test_data)
        assert responce.status_code == 302
        assert b'redirected automatically to the target URL: <a href="/">' in responce.data

    def test_route_get_doctor(self):
        responce = app.test_client().get('/doctor/?id=1')
        assert responce.status_code == 200
        assert b'Doctor record' in responce.data

    def test_route_edit_doctor(self):
        responce = app.test_client().get('/edit_doctor/?id=1')
        assert responce.status_code == 200
        assert b'Editing doctor record' in responce.data

    def test_route_edit_doctor_post(self):
        responce = app.test_client().post('/edit_doctor/', data=self.test_data)
        assert responce.status_code == 302
        assert b'redirected automatically to the target URL: <a href="/">' in responce.data

    def test_route_remove_doctor(self):
        key = self.test_data.get('email')
        responce = app.test_client().post('/remove_doctor/', data={"id": key})
        assert responce.status_code == 302
        assert b'redirected' in responce.data

    def test_route_remove_doctor_not_existed(self):
        test_data = {'id': 'notexistedid5j5k3j4j4k34'}
        responce = app.test_client().post('/remove_doctor/', data=test_data)
        assert responce.status_code == 302
        assert b'redirected' in responce.data

class TestPatientCRUD():
    ''' Testing routes for patients'''
    test_data = dict(first_name='Pedro', last_name='Sanches', gender='male', birthday='1333-08-15', email='test@email.com')
    filter_date = dict(birthday_since='1333-08-15', birthday_till='1333-08-15')
    update_data = dict(first_name='Rodrigo', last_name='Sanches', gender='male', birthday='2000-01-01', email='test@email.com')

    # delete record with test data if exist
    app.test_client().post('/delete_patient/', data={'id': test_data['email']})

    def test_route_patients(self):
        responce = app.test_client().get('/patients/')
        assert responce.status_code == 200
        assert b'List of Patients' in responce.data

    def test_route_new_patient(self):
        responce = app.test_client().get('/new_patient/?doctor_id=4')
        assert responce.status_code == 200
        assert b'Creating new patient record' in responce.data

    def test_route_new_patient_post(self):
        responce = app.test_client().post('/new_patient/', data=self.test_data)
        assert responce.status_code == 302
        assert b'redirect' in responce.data

    def test_route_patients_filter(self):
        responce = app.test_client().post('/patients/', data=self.filter_date)
        assert responce.status_code == 200
        assert b'Sanches' in responce.data

    def test_route_get_patient(self):
        responce = app.test_client().get('/patient/?id=1')
        assert responce.status_code == 200
        assert b'Patient record' in responce.data

    def test_route_edit_patient(self):
        responce = app.test_client().get('/edit_patient/?id=1')
        assert responce.status_code == 200
        assert b'Editing patient record' in responce.data

    # def test_route_edit_patient_post(self):
    #     responce = app.test_client().post('/edit_patient/', data=self.update_data)
    #     assert responce.status_code == 302
    #     assert b'redirect' in responce.data   

    def test_route_remove_patient(self):
        key = self.update_data.get('email')
        responce = app.test_client().post('/remove_patient/', data={"id": key})
        assert responce.status_code == 302
        assert b'redirected' in responce.data

    def test_route_remove_patient_not_existed(self):
        test_data = {'id': 'notexistedid',}
        responce = app.test_client().post('/remove_patient/', data=test_data)
        assert responce.status_code == 302
        assert b'redirected' in responce.data
