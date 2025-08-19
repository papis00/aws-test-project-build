import unittest
from app import say_hello

class TestApp(unittest.TestCase):
    def test_say_hello(self):
        self.assertEqual(say_hello("AWS"), "Hello, AWS")
        self.assertEqual(say_hello("Papis"), "Hello, Papis")
        self.assertEqual(say_hello("Malick"), "Hello, Malick")
        
if __name__ == "__main__":
    unittest.main()