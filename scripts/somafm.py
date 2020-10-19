import requests

from base import GenerateBase


class GenerateSomaFM(GenerateBase):

    NAME = "somafm"
    CHANNELS_JSON = "https://api.somafm.com/channels.json"

    def get(self):
        res = requests.get(self.CHANNELS_JSON)
        return {c["id"]: self.gen_channel(c) for c in res.json()["channels"]}

    def gen_channel(self, c):
        return {
            "name": c["title"],
            "description": c["description"],
            "url": c["playlists"][0]["url"],
            "tags": ["radio", "somafm"],
        }
