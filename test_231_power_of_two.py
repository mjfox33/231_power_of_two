import code_231_power_of_two as c

def test_example_1():
    s = c.Solution()
    assert s.isPowerOfTwo(1) == True

def test_example_2():
    s = c.Solution()
    assert s.isPowerOfTwo(16) == True

def test_example_3():
    s = c.Solution()
    assert s.isPowerOfTwo(3) == False

def test_my_example_1():
    s = c.Solution()
    assert s.isPowerOfTwo(15) == False