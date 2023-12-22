import logging

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
