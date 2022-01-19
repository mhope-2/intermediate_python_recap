class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value) -> None:
        self.message = message
        self.value = value

def test_value(x: int):
    if not isinstance(x, int):
        return 'Enter an integer value'
    if x > 1000:
        raise ValueTooHighError('Value should be less than or equal to 1000')
    if x < 5:
        raise ValueTooSmallError('Value should be 5 or greater.', f'Value passed: {x}')

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)