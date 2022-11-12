import os
from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options


class Driver:

    def __init__(self, download_dir, headless):
        options = Options()
        options.add_argument('--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"')
        options.add_argument('start-maximized') # Doesn't seem to work
        options.add_argument('enable-automation')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--dns-prefetch-disable')
        if headless:
            options.add_argument('--headless')
        adblocker_path = os.environ.get('ADBLOCKER_PATH')
        if adblocker_path is not None:
            options.add_extension(adblocker_path)
        prefs = {'download.default_directory': download_dir}
        options.add_experimental_option('prefs', prefs)
        options.add_experimental_option('excludeSwitches', ['enable-automation']) # Doesn't seem to work
        options.add_experimental_option('useAutomationExtension', False) # Doesn't seem to work
        self.driver = webdriver.Chrome(chrome_options=options, executable_path=os.environ['CHROMEDRIVER_PATH'])
        self.driver.implicitly_wait(10) # Seconds


    def get_driver(self):
        return self.driver

