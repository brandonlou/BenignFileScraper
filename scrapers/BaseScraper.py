from .Driver import Driver


class BaseScraper:

    def __init__(self, geckodriver, download_dir, headless=False):
        self.driver = Driver(geckodriver, download_dir, headless).get_driver()

    def __del__(self):
        self.driver.quit()

