from micropeutist_app.views.web_view import app

class TestHomeRoute():
    ''' Testing home route'''
    def test_route_home(self):
        responce = app.test_client().get('/')
        assert responce.status_code == 200
        assert b'List of Doctors' in responce.data

    def test_route_doctors(self):
        responce = app.test_client().get('/')
        assert responce.status_code == 200
        assert b'List of Doctors' in responce.data

    def test_route_new_doctor(self):
        responce = app.test_client().get('/new_doctor/')
        assert responce.status_code == 200
        assert b'Creating new doctor record' in responce.data

    def test_route_get_doctor(self):
        responce = app.test_client().get('/doctor/?id=1')
        assert responce.status_code == 200
        assert b'Doctor record' in responce.data

    def test_route_edit_doctor(self):
        responce = app.test_client().get('/edit_doctor/?id=1')
        assert responce.status_code == 200
        assert b'Editing doctor record' in responce.data

    def test_route_remove_doctor(self):
        responce = app.test_client().get('/remove_doctor/?id=some_not_existed_id')
        assert responce.status_code == 302
        assert b'redirected' in responce.data
