import os
import time
import random
from .BaseScraper import BaseScraper
from selenium.webdriver.common.by import By

START_PAGE = 11
LAST_PAGE = 800


class FileForumScraper(BaseScraper):

    def scrape(self):
        for page_num in range(START_PAGE, LAST_PAGE):
            page_link = f'https://fileforum.com/browse/windows/new/{page_num}?os=windows'
            print(f'Getting {page_link}')
            self.driver.get(page_link)
            file_list = self.driver.find_element(By.CLASS_NAME, 'fileList')
            a_tags = file_list.find_elements(By.TAG_NAME, 'a')
            file_links = []
            for a in a_tags:
                file_link = a.get_attribute('href')
                file_links.append(file_link)
            for file_link in file_links:
                try:
                    self.driver.get(file_link)
                    print(f'Getting {file_link}')
                    crumb = self.driver.find_element(By.CLASS_NAME, 'crumb')
                    category = crumb.find_element(By.TAG_NAME, 'a').text
                    download_link = file_link.replace('detail', 'download')
                    time.sleep(random.randint(5, 10))
                    success = self.download(download_link, category)
                    if not success:
                        download_link = self.driver.find_element(By.TAG_NAME, 'p').find_element(By.TAG_NAME, 'a').get_attribute('href')
                        self.download(download_link, category)
                except:
                    continue

