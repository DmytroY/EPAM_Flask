from micropeutist_app.service.service_temp import temp_func

def test_assert_pass():
    ''' test for pass '''
    assert temp_func() == "this is temp_func"

def test_assert_fail():
    ''' test for fail'''
    assert temp_func() == 43
