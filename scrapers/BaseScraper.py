from .Driver import Driver
import hashlib
import os
import pathlib
import time
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

DOWNLOAD_TIMEOUT = 90 #Seconds


class BaseScraper:

    def __init__(self, download_dir, headless=False):
        self.download_dir = download_dir
        self.driver = Driver(download_dir, headless).get_driver()

    def __del__(self):
        self.driver.quit()

    def get_sha256(self, filepath):
        h = hashlib.sha256()
        b = bytearray(128 * 1024)
        mv = memoryview(b)
        with open(filepath, 'rb', buffering=0) as f:
            while n := f.readinto(mv):
                h.update(mv[:n])
        return h.hexdigest()

    def download(self, download_link, prefix=None, click=False):
        # Get a list of files in the download directory
        files_before = dict([(f, None) for f in os.listdir(self.download_dir)])

        download_success = False

        # Some downloads do not have a URL and must be clicked on
        if click:
            try:
                download_link.click()
            except ElementClickInterceptedException:
                return False

        # Most downloads are available via a URL however
        else:
            print(f'Downloading {download_link}')
            try:
                self.driver.get(download_link)
            except TimeoutException:
                print('Download failed')
                return False

        start_time = time.time()

        while True:
            time.sleep(1)

            # Get a list of files in the download directory again
            files_after = dict([(f, None) for f in os.listdir(self.download_dir)])

            # Get a list of new files in the download directory
            new_files = [f for f in files_after if not f in files_before]

            # Found at least one new file. Download success!
            if len(new_files) > 0 and not new_files[0].endswith('.crdownload'):
                download_success = True
                break

            # Quit attempting to download if we have waited more than a certain amount of time
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time > DOWNLOAD_TIMEOUT:
                print('Download failed')
                break

        if download_success:
            # Rename downloaded file to include its hash and its category (optional)
            old_filepath = f'{self.download_dir}/{new_files[0]}'
            file_hash = self.get_sha256(old_filepath)
            file_extension = pathlib.Path(old_filepath).suffix
            if prefix:
                new_filepath = f'{self.download_dir}/{prefix}---{file_hash}{file_extension}'
            else:
                new_filepath = f'{self.download_dir}/{file_hash}{file_extension}'
            try:
                os.rename(old_filepath, new_filepath)
            except FileNotFoundError:
                print('Download failed')
                return False
            print(f'Downloaded as {new_filepath}')

        return download_success
