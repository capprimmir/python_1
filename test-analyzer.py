import os
import unittest

# move away from TDD
def analyze_text(filename):
    """Calculate the num of lines and char in a file.
    Args:
        filename: name of file o analyze
    Raises:
        IOError: if file names does not exist
    Returns: A tuple where first element is for lines and second
        is for num of characters
    """
    lines = 0
    chars = 0
    with open(filename, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
        return (lines, chars)

class TextAnalysisTest(unittest.TestCase):
    """Test for the `analyze_text()` function """

    def setUp(self):
        """Fixture that creates a file for the text methods to use"""
        self.filename = 'test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('First line test \n'
                'after line break, add another\n'
                'for testing purposes')
    
    def eraseFile(self):
        """Fixture use to delete the file created """
        try:
            os.remove(self.filename)
        except:
            pass

    # create single test, start af function with _test
    def test_function_runs(self):
        """Basic test: does the function run
        if function is undefine, test will failß"""
        analyze_text(self.filename)

    #function test that checks if line count is correct
    def test_line_count(self):
        self.assertEqual(analyze_text(self.filename)[0], 3)

    def test_char_count(self):
        """ Check character count is correct"""
        self.assertEqual(analyze_text(self.filename)[1], 67)

    def test_so_such_file(self):
        """Check proper exception is thrown for missing file """
        with self.assertRaises(IOError):
            analyze_text('foobar')

    def test_not_deletion(self):
        """ Check that the function doesn't delete file"""
        analyze_text(self.filename)
        self.assertTrue(os.path.exists(self.filename))

if __name__ == '__main__':
    # this will search for all test sub-classes and run them
    unittest.main()
    

