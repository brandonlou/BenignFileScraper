import os
import time
import random
from .BaseScraper import BaseScraper
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException , WebDriverException

START_PAGE = 149
LAST_PAGE = 800


class FileForumScraper(BaseScraper):

    def scrape(self):
        for page_num in range(START_PAGE, LAST_PAGE):
            page_link = f'https://fileforum.com/browse/windows/new/{page_num}?os=windows'
            while True:
                try:
                    print(f'Getting {page_link}')
                    self.driver.get(page_link)
                    file_list = self.driver.find_element(By.CLASS_NAME, 'fileList')
                except (TimeoutException) as e:
                    print(e)
                    continue
                break
            a_tags = file_list.find_elements(By.TAG_NAME, 'a')
            file_links = [a.get_attribute('href') for a in a_tags]
            for file_link in file_links:
                try:
                    self.driver.get(file_link)
                    print(f'Getting {file_link}')
                    crumb = self.driver.find_element(By.CLASS_NAME, 'crumb')
                    categories = crumb.find_elements(By.TAG_NAME, 'a')
                    main_category = categories[0].text
                    main_category = main_category.replace('/', '')
                    if len(categories) > 1:
                        sub_category = categories[1].text
                        sub_category = sub_category.replace('/', '')
                    else:
                        sub_category = 'None'
                    download_link = file_link.replace('detail', 'download')
                    time.sleep(random.randint(5, 10))
                    success = self.download(download_link, f'{sub_category}---{main_category}')
                    if not success:
                        download_link = self.driver.find_element(By.TAG_NAME, 'p').find_element(By.TAG_NAME, 'a').get_attribute('href')
                        self.download(download_link, f'{sub_category}---{main_category}')
                except (NoSuchElementException, TimeoutException, WebDriverException) as e:
                    print(e)

