# Benign File Scraper

## Installation
1. Install `python3.10` and `pip3`
2. Install Selenium: `pip3 install selenium-wire`
3. Install [Google Chrome](https://www.google.com/chrome/)
4. Install corresponding [ChromeDriver](https://chromedriver.chromium.org/downloads)
5. Set the `CHROMEDRIVER_PATH` environment variable to point to ChromeDriver's path.
6. Optional but recommended: Install an ad-blocker such as [uBlock Origin](https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) as a `.crx` file. Set the `ADBLOCKER_PATH` environment variable to point to the ad-blocker's path

## Usage
1. Run `python3 scraper.py <site> <download_directory>` where `site` is `fileforum`, `portablefreeware`, or `cnet`.
