from .Driver import Driver
import os
import time

DOWNLOAD_TIMEOUT = 90

class BaseScraper:

    def __init__(self, download_dir, headless=False):
        self.download_dir = download_dir
        self.driver = Driver(download_dir, headless).get_driver()

    def __del__(self):
        self.driver.quit()

    def download(self, download_link, category):
        files_before = dict([(f, None) for f in os.listdir(self.download_dir)])
        download_success = False
        print(f'Downloading {download_link}')
        self.driver.get(download_link)
        start_time = time.time()
        while True:
            time.sleep(1)
            files_after = dict([(f, None) for f in os.listdir(self.download_dir)])
            new_files = [f for f in files_after if not f in files_before]
            if len(new_files) > 0 and not new_files[0].endswith('.crdownload'):
                download_success = True
                break
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > DOWNLOAD_TIMEOUT:
                print('Download failed')
                break
        if download_success:
            filename = f'{self.download_dir}/{new_files[0]}'
            os.rename(filename, f'{filename}---{category}')
            print(f'Downloaded as {filename}')
        return download_success
