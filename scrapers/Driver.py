import os
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options


CHROMEDRIVER = '/Users/brandonlou/Projects/BenignFileScraper/chromedriver'

class Driver:

    def __init__(self, download_dir, headless):
        options = Options()
        if headless:
            options.add_argument('--headless')
        prefs = {'download.default_directory': '/Users/brandonlou/Projects/BenignFileScraper/test'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=CHROMEDRIVER)


    def get_driver(self):
        return self.driver

