import requests
from datetime import datetime
from download import download_image
import os
from dotenv import load_dotenv




def get_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"   
    payload = {"api_key": api_key, "count": 5}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for item in response.json():
        date = item.get("date")
        name = item.get("image")        
        date = datetime.fromisoformat(date).strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png?api_key={api_key}"
        download_image(url, f"images/{name}.png")


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_KEY']
    get_epic_images(api_key)