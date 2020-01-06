from BinaryAddition import add_binary


# Binary test

def test_binary():
    assert add_binary(1,1) == "10", 'Should be 10'
    assert add_binary(1, 0) == "1", 'Should be 1'
    assert add_binary(2, 2) == "100", 'Should be 100'
    assert add_binary(51, 12) == "111111", 'Should be 111111'

