import logging
import unittest

import harefully
from harefully import CallResponseTestCase, ProcessTesting, ShutdownTestCase

import keepalive

class KeepAliveTesting(ProcessTesting):
    function = keepalive.main
    args = []
    env = {}

test = CallResponseTestCase(
    '{"syn": 1, "token": "abcdef"}',
    '{"ack": 1, "token": "abcdef"}'
)

shutdown_Test = ShutdownTestCase(
    '{"shutdown": 1}'
)

KEEPALIVE_TEST = KeepAliveTesting(
    [
        test,
        shutdown_Test
    ]
)
    
@harefully.test_case
class KeepAliveTestCase(unittest.TestCase):
    function = keepalive.main
    tests = [test, shutdown_Test]

    def test_woop(self):
        self.assertTrue(False)

