import re
from .BaseScraper import BaseScraper
from time import sleep


START_PAGE = 0
NUM_PAGES = 242

class DownloadCrewScraper(BaseScraper):

    def scrape(self):
        for page_num in range(START_PAGE, NUM_PAGES):
            self.driver.get('https://downloadcrew.com')
            script = f'''
            var xhr = new XMLHttpRequest();
            xhr.open("POST", "https://downloadcrew.com/", false);
            xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded; charset=UTF-8");
            xhr.send("act=software.downloads&page={page_num}&orderBy=pubDate&orderDesc=desc&rating=&license=&category=&type=latest");
            return xhr.response;
            '''
            response = self.driver.execute_script(script)
            product_links = re.findall(r'<div class="productListing">\s*<a href="(.*?)">', response)
            download_links = [link.replace('article', 'download') for link in product_links]
            for download_link in download_links:
                self.driver.get(download_link)
                sleep(30)
        sleep(120)

