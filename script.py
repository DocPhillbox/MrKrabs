import requests
from bs4 import BeautifulSoup
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', help="The url where dowload media file", type=str)
args = vars(parser.parse_args())

def get_html_from_url(url: str):
    req = requests.get(url)
    return req.text

htmldata = get_html_from_url(args['url'] or "https://www.geeksforgeeks.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
for image in soup.find_all('img'):
    image_src = image.get('src')
    if image_src:
        print('download file:', image_src)
        image_name = Path(image_src).name
        image_data = requests.get(image_src).content
        open('out/' + image_name, 'wb').write(image_data)