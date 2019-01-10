import unittest, time
from time import sleep

# utils
from selenium_qa_sandbox.seleniumBase import SeleniumBase


class Example(SeleniumBase):

    test_feature = 'Example'

    def test_1(self):
        self.test_case = 'Example 1'
        sleep(6)
        pass
        

if __name__ == '__main__':
    unittest.main()
