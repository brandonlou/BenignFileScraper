from .BaseScraper import BaseScraper
from time import sleep


START_PAGE = 0
LAST_PAGE = 1884

class MajorGeeksScraper(BaseScraper):

    def scrape(self):
        seen_files = set()
        for page_num in range(START_PAGE, LAST_PAGE):
            page_link = f'https://www.majorgeeks.com/files/page/{page_num}.html'
            print(f'Getting {page_link}')
            self.driver.get(page_link)
            file_links = []
            geekytitles = self.driver.find_elements_by_class_name('geekytitle')
            for geekytitle in geekytitles:
                a = geekytitle.find_element_by_tag_name('a')
                file_link = a.get_attribute('href')
                file_links.append(file_link)
            for file_link in file_links:
                if file_link in seen_files: # Don't repeat downloads
                    continue
                print(f'Getting {file_link}')
                seen_files.add(file_link)
                file_name = file_link[41:-5]
                self.driver.get(f'https://www.majorgeeks.com/mg/getmirror/{file_name},1.html')
                sleep(30)
        sleep(120) # Wait for last download to complete

