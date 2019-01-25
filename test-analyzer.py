import unittest

class TextAnalysisTest(unittest.TestCase):
    """Test for the `analyze_text()` function """

    # create single test, start af function with _test
    def test_function_runs(self):
        """Basic test: does the function run
        if function is undefine, test will failß"""
        analyze_text()

if __name__ == '__main__':
    # this will search for all test sub-classes and run them
    unittest.main()
    
