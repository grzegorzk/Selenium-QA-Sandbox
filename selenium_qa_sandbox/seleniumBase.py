import sys, os, unittest, configparser, re, datetime

# selenium base
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumBase(unittest.TestCase):
    ini_file = "selenium.ini"
    config = None
    test_feature = None
    test_case = None

    def setConfig(self):
        new_config = configparser.ConfigParser()
        new_config.read(self.ini_file)
        self.config = new_config

    def setBrowser(self):
        if 'app' not in self.config:
            self.print_error("Malformed `selenium.ini`, terminating.")
            exit(1)
        if self.config['app'].get('browser') == 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--window-size={},{}".format(
                self.config['screen']['width'],
                self.config['screen']['height']))
            self.browser = webdriver.Chrome(
                self.config['browser.chrome']['path'],
                desired_capabilities=chrome_options.to_capabilities())
        else:
            self.print_error('Invalid browser: '
                + self.config['app'].get('browser'))
            exit(1)

        # set window size
        if 'screen' in self.config:
            self.browser.set_window_position(0, 0)
            self.browser.set_window_size(
                self.config['screen'].get('width'),
                self.config['screen'].get('height'))

    def setUp(self, do_login = True):
        # set config
        self.setConfig()

        # set browser
        self.setBrowser()

        # add utilities to class
        self.wait = WebDriverWait(self.browser, 20)  # maximum waiting time in seconds
        self.EC = EC
        self.By = By
        self.Keys = Keys
        self.browser.get(self.config['app'].get('url'))

    def tearDown(self):
        self.browser.quit()

    def run(self, result=None):
        unittest.TestCase.run(self, result) # call superclass run method

    def print_error(self, text):
        print(Fore.RED + Style.BRIGHT + text + Style.RESET_ALL)
