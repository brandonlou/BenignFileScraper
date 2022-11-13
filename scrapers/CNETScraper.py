import os
import time
import random
from .BaseScraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from urllib.parse import unquote
START_PAGE = 200
LAST_PAGE = 6371

class CNETScraper(BaseScraper):

    def find_existing_links(self):
        link_delim = '---___---'
        existing_links = dict([(unquote(f.split(link_delim)[0]), None) for f in os.listdir(self.download_dir) if link_delim in f ])
        
        return existing_links

    def scrape(self):
        existing_links = self.find_existing_links()
        
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
                if product_link in existing_links:
                    print(f'Already Downloaded {product_link}')
                    continue
                    
                print(f'Downloading {product_link}')
                try:
                    self.driver.get(product_link)
                except TimeoutException as e:
                    print(e)
                    continue

                #try to get the category
                prefix = None
                try:
                    category_crumb = self.driver.find_element(By.CLASS_NAME, 'c-navigationBreadcrumb')
                    categories = category_crumb.find_elements(By.TAG_NAME, 'a')
                    prefix = '---'.join([category.text for category in categories])
                    
                    link = product_link.replace('/', '%2F')
                    prefix = link + '---___---' + prefix
                    
                    print(prefix)
                except NoSuchElementException as e:
                    print(e)
                    
                #exit()
                try:
                    download_button = self.driver.find_element(By.CLASS_NAME, 'c-productActionButton_text')
                    self.download(download_button, click=True, prefix=prefix)
                except NoSuchElementException as e:
                    print(e)

