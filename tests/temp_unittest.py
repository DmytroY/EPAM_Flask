# '''testing of unittest '''
# import unittest

from micropeutist_app.service.service_temp import temp_func

#import sys
#sys.path.append('../')

class TestTemp(unittest.TestCase):
    '''probational testing'''

    def test_temp_func(self):
        '''testcase for service_temp.temp_func'''
        self.assertEqual(temp_func(), "this is temp_func")


if __name__ == '__main__':
    unittest.main()
