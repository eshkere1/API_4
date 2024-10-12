import requests
import os
from urllib.parse import urlparse, unquote
from download import download_image
from dotenv import load_dotenv




def get_extension(url):
    url = unquote(url)
    parseurl = urlparse(url)
    directory, filename = os.path.split(parseurl.path)
    name, extension = os.path.splitext(filename)
    return name, extension

    
def get_photo_apod(folder, api_key, num=5):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"count": num, "api_key": api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for item in response.json():
        if item.get('media_type') == 'image':
            apod_url = item.get("hdurl") or item.get("url")
            name, extension = get_extension(apod_url)
            path = os.path.join(folder,f"{name}{extension}")
        download_image(apod_url, path)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    get_photo_apod("images", api_key, num=5)
    