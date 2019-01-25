import os
import unittest

# empty function to pass the test
def analyze_text(filename):
    pass

class TextAnalysisTest(unittest.TestCase):
    """Test for the `analyze_text()` function """

    def setUp(self):
        """Fixture that creates a file for the text methods to use"""
        self.filename = 'test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('This is the first line test \n'
                'after line break, add another line \n'
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
        self.assertEqual(analyze_text(self.filename), 3)

if __name__ == '__main__':
    # this will search for all test sub-classes and run them
    unittest.main()
    

