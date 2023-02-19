from micropeutist_app.application import app
def test_home_route():
    responce = app.test_client().get('/')
    print(responce)

test_home_route()