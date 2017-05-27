import requests
from bs4 import BeautifulSoup
import re

HOME_URL = "http://zineblog.com.tw/blog/post/45501739"
HTML_PARSER = "html.parser"

def get_link_list():
    list_req = requests.get(HOME_URL)
    if list_req.status_code == requests.codes.ok:
        soup = BeautifulSoup(list_req.content, HTML_PARSER)
        links = soup.find_all('a', href = True, text = re.compile('【'))

        for link in links:
            print(link.text)
            print(link['href'])
            get_information(link['href'])

def get_information(link):
    req = requests.get(link)
    if req.status_code == requests.codes.ok:
        soup = BeautifulSoup(req.content, HTML_PARSER)
        addresses = soup.find_all(text = re.compile('地址:'))

        print(len(addresses))
        for address in addresses:
            print(str(address) + '\n')

if __name__ == '__main__':
    get_link_list()