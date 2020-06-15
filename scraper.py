from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

import requests
import os
import time
import checkname

class scraper(object):

    def __init__(self):
        self.perc_downloaded = 0
        print("Nhentai-Scraper initialized")

    def get_perc (self):
        return self.perc_downloaded

    def scrape_comic(self, nh_index):
        url = "https://nhentai.net/g/{0}/".format(nh_index)
        if requests.get(url).status_code == 200:
            f = requests.get(url).text
            soup = BeautifulSoup(f, 'html5lib')

            cover_meta_title = soup.find('meta', {"itemprop" : "name"})
            cover_name = cover_meta_title.get('content')
            cover_meta_image = soup.find('meta', {"itemprop" : "image"})
            cover_link = cover_meta_image.get('content')

            cover_name = checkname.fixname(cover_name)
            dir_loc = os.path.expanduser("~/Desktop")
            folder = '{0}/{1}'.format(dir_loc, cover_name)
            os.mkdir(folder)

            try:
                cover_request = requests.get(cover_link).content
                cover_image_buffer = BytesIO(cover_request)
                cover_image = Image.open(cover_image_buffer).convert("RGBA")
                cover_image.save("{0}/cover.png".format(folder))
            except:
                print()

            _index = 0
            manga_length = len(soup.find_all('div', {"class" : "thumb-container"}))

            for i in soup.find_all('div', {"class" : "thumb-container"}):

                time.sleep(0.25)

                img_link = 'https://nhentai.net' + i.a.get('href')
                page_req = requests.get(img_link).text
                img_soup = BeautifulSoup(page_req, 'html5lib')

                _link = img_soup.find('section', {"id" : "image-container"}).a.img.get('src')

                _index += 1

                try:
                    r = requests.get(_link).content
                    img_data_buffer = BytesIO(r)
                    img = Image.open(img_data_buffer).convert("RGBA")
                    img.save("{0}/{1}.png".format(folder, _index))

                    self.perc_downloaded = (_index / manga_length) * 100
                except:
                    print()