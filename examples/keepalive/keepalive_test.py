from harey import CallResponseTestCase, ProcessTesting

class KeepAliveTesting(ProcessTesting):
    process_name = "keepalive.py"
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

