import unittest

def digits(x):
    """Convert integer into a list of digits,

    Args:
        x: The number to convert
    Returns:
        List of digits in order

    >>> digits(474648)
    [4,7,4,6,4,8]
    """

    digsList = []
    while x != 0:
        div, mod = divmod(x, 10)
        digsList.append(mod)
        x = div
    return digsList

def is_palindrome(x):
    """Determine if a number is palindrome.

    Args: 
        x: the number to check

    Return:
        true oif list of numbers is palindrome
        """

    digsList = digits(x)
    for f, r in zip(digsList, reversed(digsList)):
        if f != r:
            return False
    return True

# set of unit test 
class Tests(unittest.TestCase):
    def test_negative(self):
        # check that returns False correctly
        self.assertFalse(is_palindrome(1234))
    
    def test_positive(self):
        # check if returns True correctly
        self.assertTrue(is_palindrome(1234321))

    def test_single_digit(self):
        #check it works for single digit
        for i in range(10):
            self.assertTrue(is_palindrome(i))

if __name__ == '__main__':
    unittest.main()

