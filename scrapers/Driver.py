import os
from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options


class Driver:

    def __init__(self, geckodriver, download_dir, headless):
        options = Options()
        options.set_preference('browser.download.folderList', 2)
        options.set_preference('browser.download.useDownloadDir', True)
        options.set_preference('browser.download.viewableInternally.enabledTypes', '')
        options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream,application/x-msdownload,application/x-ms-installer,application/vnd.microsoft.portable-executable,application/zip,application/vnd.rar,application/x-7z-compressed,application/x-msdos-program,rar,ZIP,BZ2,exe')
        options.set_preference('browser.download.dir', download_dir)
        if headless:
            options.add_argument('--headless')
        self.driver = webdriver.Firefox(options=options, executable_path=geckodriver, service_log_path=os.devnull)

    def get_driver(self):
        return self.driver

