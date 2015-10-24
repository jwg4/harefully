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
    
if __name__ == '__main__':
    KEEPALIVE_TEST.run_test()

