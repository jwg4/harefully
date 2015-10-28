import unittest

import inspect

from harefully import test_case

class TestUnittest(unittest.TestCase):
    """ Tests the function which makes a unittest test case from a class."""
    def test_creates_a_subclass_of_unittest__TestCase(self):
        """ Check that the decorated class is a subclass of unittest.TestCase._"""
        a = object
        tc = test_case(a)
        self.assertTrue(issubclass(tc, unittest.TestCase))

    def test_creates_a_test_function(self):
        """ Check that we get at least one function whose name starts with 'test_' in the decorated class."""
        a = object
        tc = test_case(a)
        methods = inspect.getmembers(tc, predicate=inspect.ismethod)
        test_methods = [ m for m in methods if m[0].startswith('test_') ]
        self.assertTrue(len(test_methods) > 0)

