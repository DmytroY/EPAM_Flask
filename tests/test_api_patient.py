from micropeutist.application import app


class TestApiGetPatients():
    ''' Testing route /api/patients/'''
    def test_get_api_patients(self):
        response = app.test_client().get('/api/patients/')
        assert response.status_code == 200

class TestApiPatientCRUD():
    ''' testing CRUP operations by API'''
    test_data = dict(first_name='Pedro', last_name='Sanches', gender='male', birthday='1333-08-15', email='test@email.com')
    filter_date = dict(birthday_since='1333-08-15', birthday_till='1333-08-15')
    update_data = dict(first_name='Rodrigo', last_name='Sanches', gender='male', birthday='2000-01-01', email='test@email.com')
    notexist_data = dict(first_name='a', last_name='b', gender='c', birthday='2000-01-01', email='no@email.com')
    
    # delete record with test data if exist
    app.test_client().delete('/api/delete_patient/', json={'id': test_data['email']})
    
    def test_api_create_patient(self):
        response = app.test_client().post('/api/create_patient/', json=self.test_data)
        assert response.status_code == 201
        assert b'have been added' in response.data

    def test_api_create_patient_duble(self):
        response = app.test_client().post('/api/create_patient/',json=self.test_data)
        assert response.status_code == 409
        assert b'Error. This email already exist in Patient records' in response.data

    def test_api_patient_filter_by_date(self):
        response = app.test_client().post('/api/patients/', json=self.filter_date)
        response = app.test_client().post('/api/patients/', json=self.filter_date)
        assert response.status_code == 200
        assert b'Sanches' in response.data
        assert b'specialization' not in response.data

    def test_api_receive_patient_by_email(self):
        response = app.test_client().get('/api/receive_patient/?id=test@email.com')
        assert response.status_code == 200  
        assert b'Sanches' in response.data

    def test_api_receive_patient_by_id(self):
        response = app.test_client().get('/api/receive_patient/?id=test@email.com')
        id = response.get_json().get('id')
        response = app.test_client().get('/api/receive_patient/?id=' + str(id))
        assert response.status_code == 200  
        assert b'Sanches' in response.data

    def test_api_receive_not_existed_patient(self):
        response = app.test_client().get('/api/receive_patient/?id=some_not_existed_key_4n2k2n42')
        assert response.status_code == 204 

    def test_api_update_patient(self):
        response = app.test_client().put('/api/update_patient/', json=self.update_data)
        assert response.status_code == 201
        assert b'have been updated' in response.data

    def test_api_update_patient_not_existing(self):
        response = app.test_client().put('/api/update_patient/', json=self.notexist_data)
        assert response.status_code == 409
        assert b'Error. No record with such key' in response.data

    def test_api_delete_patient(self):
        response = app.test_client().delete('/api/delete_patient/', json={'id': self.test_data['email']})
        assert response.status_code == 200
        assert b'have been deleted' in response.data

    def test_api_delete_patient_not_existing(self):
        response = app.test_client().delete('/api/delete_patient/', json={'id': self.notexist_data['email']})
        assert response.status_code == 409
        assert b'No such patient record in the database' in response.data
