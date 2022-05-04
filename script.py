import requests
from bs4 import BeautifulSoup
from pathlib import Path

def get_html_from_url(url: str):
    req = requests.get(url)
    return req.text

htmldata = get_html_from_url("https://www.geeksforgeeks.org/")
soup = BeautifulSoup(htmldata, 'html.parser')
for image in soup.find_all('img'):
    image_src = image.get('src')
    image_name = Path(image_src).name
    image_data = requests.get(image_src).content
    open('out/' + image_name, 'wb').write(image_data)