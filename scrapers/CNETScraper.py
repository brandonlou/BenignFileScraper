import os
import time
import random
from .BaseScraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

START_PAGE = 4
LAST_PAGE = 6371

class CNETScraper(BaseScraper):

    def scrape(self):
        for page_num in range(START_PAGE, LAST_PAGE):
            website = f'https://download.cnet.com/windows/{page_num}/?sort=newReleases&price=free&price=freeToTry'
            print(f'Getting {website}')
            self.driver.get(website)
            productCardLinks = self.driver.find_elements(By.CLASS_NAME, 'c-productCard_link')
            product_links = set()
            for pcl in productCardLinks:
                product_link = pcl.get_attribute('href')
                product_links.add(product_link)
            for product_link in product_links:
                print(f'Downloading {product_link}')
                try:
                    self.driver.get(product_link)
                except TimeoutException as e:
                    print(e)
                    continue
                try:
                    download_button = self.driver.find_element(By.CLASS_NAME, 'c-productActionButton_text')
                    self.download(download_button, click=True)
                except NoSuchElementException as e:
                    print(e)

