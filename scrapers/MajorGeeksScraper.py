from .BaseScraper import BaseScraper
from time import sleep
from selenium.webdriver.common.by import By


START_PAGE = 0
LAST_PAGE = 2053

class MajorGeeksScraper(BaseScraper):

    def scrape(self):
        seen_files = set()
        for page_num in range(START_PAGE, LAST_PAGE):
            page_link = f'https://www.majorgeeks.com/files/page/{page_num}.html'
            print(f'Getting {page_link}')
            self.driver.get(page_link)
            file_links = []
            geekytitles = self.driver.find_elements(By.CLASS_NAME, 'geekytitle')
            for geekytitle in geekytitles:
                a = geekytitle.find_element(By.TAG_NAME, 'a')
                file_link = a.get_attribute('href')
                file_links.append(file_link)
            for file_link in file_links:
                if file_link in seen_files: #Don't repeat downloads
                    continue
                seen_files.add(file_link)
                print(f'Getting {file_link}')
                self.driver.get(file_link)
                category = self.driver.find_element(By.CLASS_NAME, 'navigation').find_elements(By.TAG_NAME, 'a')[1].text
                file_name = file_link[41:-5]
                download_link = f'https://www.majorgeeks.com/mg/getmirror/{file_name},1.html'
                success = self.download(download_link, category)
                if not success:
                    self.download('https://www.majorgeeks.com/index.php?ct=files&action=download&', category)
