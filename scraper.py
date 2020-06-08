from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os

class scraper(object):

    def __init__(self):
        print("Nhentai-Scraper initialized")

    def scrape_comic(self, nh_index):
        url = "https://nhentai.net/g/{0}/".format(nh_index)
        if requests.get(url).status_code == 200:
            f = requests.get(url).text
            soup = BeautifulSoup(f, 'html5lib')

            cover_meta_title = soup.find('meta', {"itemprop" : "name"})
            cover_name = cover_meta_title.get('content')
            cover_meta_image = soup.find('meta', {"itemprop" : "image"})
            cover_link = cover_meta_image.get('content')

            os.mkdir(cover_name)

            try:
                cover_request = requests.get(cover_link).content
                cover_image_buffer = BytesIO(cover_request)
                cover_image = Image.open(cover_image_buffer).convert("RGBA")
                cover_image.save("{0}/cover.png".format(cover_name))
            except:
                print()

            _index = 0
            for i in soup.find_all('div', {"class" : "thumb-container"}):
                img_link = 'https://nhentai.net' + i.a.get('href')
                page_req = requests.get(img_link).text
                img_soup = BeautifulSoup(page_req, 'html5lib')

                _link = img_soup.find('section', {"id" : "image-container"}).a.img.get('src')

                _index += 1

                try:
                    r = requests.get(_link).content
                    img_data_buffer = BytesIO(r)
                    img = Image.open(img_data_buffer).convert("RGBA")
                    img.save("{0}/{1}.png".format(cover_name, _index))
                    # print percent downloaded
                except:
                    print()