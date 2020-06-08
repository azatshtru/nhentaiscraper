import scraper

_scraper = scraper.scraper()

nh_index = input("Enter the N-hentai index/number of comic: ")

_scraper.scrape_comic(nh_index)