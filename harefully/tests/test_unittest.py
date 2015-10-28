import unittest

from harefully import test_case

class TestUnittest(unittest.TestCase):
    """ Tests the function which makes a unittest test case from a class."""
    def test_test_case(self):
        a = object
        tc = test_case(a)
        self.assertTrue(issubclass(tc, unittest.TestCase))

