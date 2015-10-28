import logging

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
    
@harefully.test_case(KEEPALIVE_TEST):
class KeepAliveTestCase(object):
    function = keepalive.main
    tests = [test]

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    KEEPALIVE_TEST.run_test()

