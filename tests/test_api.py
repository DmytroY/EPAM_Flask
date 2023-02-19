from micropeutist_app.application import app

def test_get_api_home():
    with app.test_client() as c:
        responce = c.get('/api')
        #json_responce = responce.get_json()
        #print(json_responce)
        assert responce.status_code == 200

#test_get_api_home()