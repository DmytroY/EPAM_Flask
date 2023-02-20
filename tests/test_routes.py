from EPAM_Flask.micropeutist_app.views.web_view import app


def test_home_route():
    responce = app.test_client().get('/')
    assert responce.status_code == 200
    assert b'<p>List of Doctors</p>' in responce.data

#     print("=== test_home_route responce === :", responce)
#     print("=== responce.data ==== ", responce.data)

# test_home_route()
