from EPAM_Flask.micropeutist_app.rest.api_view import app

def test_get_api_home():
    responce = app.test_client().get('/api')
    assert responce.status_code == 200

#     json_responce = responce.get_json()
#     print("=== json_responce:", json_responce)
#     print("=== responce.status_code:", responce.status_code)
        

# test_get_api_home()