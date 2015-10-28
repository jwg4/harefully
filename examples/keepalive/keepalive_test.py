import logging
import unittest

import harefully
from harefully import CallResponseTestCase, ProcessTesting

import keepalive

class KeepAliveTesting(ProcessTesting):
    function = keepalive.main
    args = []
    env = {}

test = CallResponseTestCase(
    '{"syn": 1, "token": "abcdef"}',
    '{"ack": 1, "token": "abcdef"}'
)

KEEPALIVE_TEST = KeepAliveTesting(
    [
        test
    ]
)
    
@harefully.test_case
class KeepAliveTestCase(unittest.TestCase):
    function = keepalive.main
    tests = [test]

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    KEEPALIVE_TEST.run_test()

