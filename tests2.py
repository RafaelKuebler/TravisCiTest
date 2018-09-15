import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertNotEqual(fun(3), 4)
        
if __name__ == '__main__':
    unittest.main()
