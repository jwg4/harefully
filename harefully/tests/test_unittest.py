import unittest

from harefully import test_case

class TestUnittest(unittest.TestCase):
    """ Tests the function which makes a unittest test case from a class."""
    def test_creates_a_subclass_of_unittest__TestCase(self):
        a = object
        tc = test_case(a)
        self.assertTrue(issubclass(tc, unittest.TestCase))

