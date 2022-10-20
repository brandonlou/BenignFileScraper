import os
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:

    def __init__(self, download_dir, headless):
        options = Options()
        options.add_argument('start-maximized') #doesn't seem to work
        options.add_argument('enable-automation')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        if headless:
            options.add_argument('--headless')
        options.add_extension('/Users/brandonlou/Downloads/ublock.crx')
        prefs = {'download.default_directory': download_dir}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=os.environ['CHROMEDRIVER_PATH'])


    def get_driver(self):
        return self.driver

