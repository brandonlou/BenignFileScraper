from .BaseScraper import BaseScraper
from time import sleep


START_PAGE = 0
LAST_PAGE = 800

class FileForumScraper(BaseScraper):

    def scrape(self):
        for page_num in range(START_PAGE, LAST_PAGE):
            page_link = f'https://fileforum.com/browse/windows/new/{page_num}?os=windows'
            print(f'Getting {page_link}')
            self.driver.get(page_link)
            file_list = self.driver.find_element_by_class_name('fileList')
            a_tags = file_list.find_elements_by_tag_name('a')
            file_links = []
            for a in a_tags:
                file_link = a.get_attribute('href')
                file_links.append(file_link)
            for file_link in file_links:
                download_link = file_link.replace('detail', 'download')
                print(f'Getting {download_link}')
                self.driver.get(download_link)
                sleep(30)
        sleep(120)

