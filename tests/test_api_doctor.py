from micropeutist_app.rest.api_view import app


class TestApiHome():
    ''' Testing home routes'''
    def test_get_api_home(self):
        assert app.test_client().get('/api/').status_code == 200

class TestApiGetDoctors():
    ''' Testing route /api/doctors'''
    def test_get_api_doctors(self):
        response = app.test_client().get('/api/doctors/')
        assert response.status_code == 200

class TestApiDoctorCRUD():
    ''' testing CRUP operations by API'''
    test_data = dict(first_name='Pedro', last_name='Sanches', grade='TG', specialization='ts', email='test@email.com')
    update_data = dict(first_name='Rodrigo', last_name='Sanches', grade='TG', specialization='ts', email='test@email.com')
    notexist_data = dict(first_name='a', last_name='b', grade='c', specialization='d', email='no@email.com')
    
    # delete record with test data if exist
    app.test_client().delete('/api/delete_doctor/', json={'id': test_data['email']})
    
    def test_api_create_doctor(self):
        response = app.test_client().post('/api/create_doctor/',json=self.test_data)
        assert response.status_code == 201
        assert b'have been added' in response.data

    def test_api_create_doctor_duble(self):
        response = app.test_client().post('/api/create_doctor/',json=self.test_data)
        assert response.status_code == 409
        assert b'Error. This email already exist in Doctor records' in response.data

    def test_api_receive_doctor_by_email(self):
        response = app.test_client().get('/api/receive_doctor/?id=test@email.com')
        assert response.status_code == 200  
        assert b'Sanches' in response.data

    def test_api_receive_doctor_by_id(self):
        response = app.test_client().get('/api/receive_doctor/?id=test@email.com')
        id = response.get_json().get('id')
        response = app.test_client().get('/api/receive_doctor/?id=' + str(id))
        assert response.status_code == 200  
        assert b'Sanches' in response.data

    def test_api_update_doctor(self):
        response = app.test_client().put('/api/update_doctor/', json=self.update_data)
        assert response.status_code == 201
        assert b'have been updated' in response.data

    def test_api_update_doctor_not_existing(self):
        response = app.test_client().put('/api/update_doctor/', json=self.notexist_data)
        assert response.status_code == 409
        assert b'Error. No record with such key' in response.data

    def test_api_delete_doctor(self):
        response = app.test_client().delete('/api/delete_doctor/', json={'id': self.test_data['email']})
        assert response.status_code == 200
        assert b'have been deleted' in response.data

    def test_api_delete_doctor_not_existing(self):
        response = app.test_client().delete('/api/delete_doctor/', json={'id': self.notexist_data['email']})
        assert response.status_code == 409
        assert b'No such doctor record in the database' in response.data
