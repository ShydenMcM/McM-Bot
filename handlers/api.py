import json
import logging
import random

import requests

import settings

config = settings.Config().load()


class Kawaii:
    def __init__(self, **kwargs):
        self.base_url = "https://kawaii.red/api/gif/"
        self.token = str(config.KAWAII_API_TOKEN)

    def get_gif(self, action: str, **kwargs):
        url = f"{self.base_url}{action}/token={self.token}&type=txt"
        if kwargs.get("excludes"):
            url = url + f'&filter={kwargs.get("excludes")}'
        gif_url_response = requests.get(url=url)
        assert gif_url_response.status_code == 200
        gif_url = gif_url_response.text.replace('"', '')
        logging.debug("GIF: %s", gif_url)
        return gif_url


class Tenor:
    def __init__(self, **kwargs):
        self.base_url = "https://tenor.googleapis.com/v2/"
        self.token = str(config.TENOR_API_KEY)
        self.client_key = "mcm-bot-1670960368647"

    def search_gif(self, search: str, **kwargs):
        response = requests.get(
            f"{self.base_url}search?q={search}&key={self.token}&client_key={self.client_key}&limit=5"
        )
        # load the GIFs using the urls for the smaller GIF sizes
        gifs = json.loads(response.content)["results"]
        urls = []
        for gif in gifs:
            urls.append(gif["media_formats"]["gif"]["url"])
        return random.choice(urls)


if __name__ == "__main__":
    tenor = Tenor()
    print(tenor.search_gif(search="you murderer"))
