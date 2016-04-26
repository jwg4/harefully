import logging

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

shutdown_test = ShutdownTestCase(
    '{"shutdown": 1}'
)

KEEPALIVE_TEST = KeepAliveTesting(
    [
        test,
        shutdown_test
    ]
)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    KEEPALIVE_TEST.run_test()

