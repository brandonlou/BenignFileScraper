import argparse
from scrapers import DownloadCrewScraper, FileForumScraper, MajorGeeksScraper


def main():
    parser = argparse.ArgumentParser(description='Benign file scraper')
    parser.add_argument('geckodriver', help='path to geckodriver')
    parser.add_argument('site', help='site to scrape (downloadcrew, fileforum, or majorgeeks)')
    parser.add_argument('download-dir', help='path to download directory')
    parser.add_argument('--headless', dest='headless', action='store_true', help='run browser headless')
    args = parser.parse_args()
    if args.site == 'downloadcrew':
        scraper = DownloadCrewScraper(args.geckodriver, args.download_dir, args.headless)
    elif args.site == 'fileforum':
        scraper = FileForumScraper(args.geckodriver, args.download_dir, args.headless)
    elif args.site == 'majorgeeks':
        scraper = MajorGeeksScraper(args.geckodriver, args.download_dir, args.headless)
    else:
        print('Error: Invalid site')
        exit()
    scraper.scrape()
    print('Done.')


if __name__ == '__main__':
    main()

