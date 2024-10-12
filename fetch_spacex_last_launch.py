import requests
from download import download_image
import argparse




def fetch_spacex_last_launch(launch_id):
    url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for index, item in enumerate(links, start=1):
        download_image(item, f"images/spacex{index}.png")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Данный скрипт позволяет скачать картинки по ID его запуска")
    parser.add_argument("--ID", help="Введите ID запуска", type=str, default="5eb87d47ffd86e000604b38a")
    args = parser.parse_args()
    launch_id = args.ID
    fetch_spacex_last_launch(launch_id)
