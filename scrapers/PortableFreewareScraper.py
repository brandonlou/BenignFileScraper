import os
import time
import random
from .BaseScraper import BaseScraper
from selenium.webdriver.common.by import By

START_PAGE = 12
LAST_PAGE = 100


class PortableFreewareScraper(BaseScraper):
    def scrape(self):
        for page_num in range(START_PAGE, LAST_PAGE):
            website = f'https://www.portablefreeware.com/index.php?p={page_num}&s=25'
            print(f'Getting {website}')
            self.driver.get(website)
            download_links = set()
            li_list = self.driver.find_elements(By.CLASS_NAME, 'download')
            for li in li_list:
                a_list = li.find_elements(By.CLASS_NAME, 'external')
                for a in a_list:
                    download_link = a.get_attribute('title')
                    download_links.add(download_link)
            for download_link in download_links:
                self.download(download_link)
