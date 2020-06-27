import unittest
import main

#in comand line python3 -m unittest -v

class TestMain(unittest.TestCase):

    def setUp(self):
        print('about a test funtion')

    def test_do_stuff(self):
        testparam = 10
        result = main.do_stuff(testparam)
        self.assertEqual(result, 15)
    
    def test2(self):
        testparam = 40
        result = main.do_stuff(testparam)
        self.assertEqual(result, 45)

    def test_do_stuff2(self):
        testparam = 'sssss'
        result = main.do_stuff(testparam)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result,'please enter a number' )

    def test_do_stuff4(self):
            test_param = ''
            result = main.do_stuff(test_param)
            self.assertEqual(result,'please enter a number')
    
    def tearDown(self):
        print('cleaning up')
        
if __name__ == '__main__':
    unittest.main() 
