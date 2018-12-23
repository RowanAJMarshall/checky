import unittest

from checky import check

class BasicCheckyTests(unittest.TestCase):

    # Sanity tests

    def test_no_args_or_return(self):
        @check(returns = None)
        def no_args_or_return():
            return None
        no_args_or_return()

    def test_more_arguments_than_types(self):
        @check(args = [int, str])
        def more_arguments_than_types(s):
            pass
        with self.assertRaises(Exception):
            more_arguments_than_types()

    # Positive tests

    def test_return_right_type(self):
        @check(returns = int)
        def return_right_type():
            return 1
        return_right_type()

    def test_takes_right_type(self):
        @check(args = [int])
        def takes_right_type(num):
            pass
        takes_right_type(1)

    def test_takes_and_returns_right_type(self):
        @check(args = [int], returns = int)
        def takes_and_returns_right_type(num):
            return 1

    def test_takes_right_keyword_type(self):
        @check(kwargs = {"name": str})
        def takes_right_keyword_type(name=""):
            pass
        takes_right_keyword_type(name="checky")

    # Negative tests

    def test_return_wrong_type(self):
        @check(returns = str)
        def return_wrong_type():
            return 1
        with self.assertRaises(AssertionError):
            return_wrong_type()

    def test_wrong_type(self):
        @check(args = [int])
        def takes_wrong_type(word):
            pass
        with self.assertRaises(AssertionError):
            takes_wrong_type("spam")

    def test_wrong_keyword_argument_type(self):
        @check(kwargs = {"name": str})
        def takes_wrong_keyword_argument_type(name=""):
            pass
        with self.assertRaises(AssertionError):
            takes_wrong_keyword_argument_type(name=1)

    
if __name__ == '__main__':
    unittest.main()