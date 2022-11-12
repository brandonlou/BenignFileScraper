import argparse
from scrapers import CNETScraper, FileForumScraper, PortableFreewareScraper


def main():
    parser = argparse.ArgumentParser(description='Benign file scraper')
    parser.add_argument('site', help='website to scrape (fileforum, portablefreeware, cnet)')
    parser.add_argument('download_dir', metavar='download-dir', help='absolate path to download directory')
    parser.add_argument('--headless', dest='headless', action='store_true', help='run browser headless')
    args = parser.parse_args()
    if args.site == 'fileforum':
        scraper = FileForumScraper(args.download_dir, args.headless)
    elif args.site == 'portablefreeware':
        scraper = PortableFreewareScraper(args.download_dir, args.headless)
    elif args.site == 'cnet':
        scraper = CNETScraper(args.download_dir, args.headless)
    else:
        print('Error: Invalid site')
        exit()
    scraper.scrape()
    print('Done.')


if __name__ == '__main__':
    main()

