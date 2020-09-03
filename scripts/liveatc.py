import re
import requests

from bs4 import BeautifulSoup
from base import GenerateBase

FEED_TYPES = [
    # "class-b",
    # "class-c",
    # "class-d",
    # "us-artcc",
    # "canada",
    # "international-eu",
    # "international-oc",
    # "international-as",
    # "international-sa",
    # "international-na",
    "international-af",
    "hf",
]


class GenerateLiveATC(GenerateBase):

    NAME = "liveatc"
    BASE_FEED_URL = "https://www.liveatc.net/feedindex.php"

    def get(self):
        for feed in FEED_TYPES:
            print(feed)
            res = requests.get(self.BASE_FEED_URL, params={"type": feed})
            soup = BeautifulSoup(res.content)
            print(soup.prettify())
            # pattern = r"""<a onClick="myDirectStream\('([^\)]*)'\)">([^<]*)<\/a>"""
            # matches = re.findall(pattern, res)
            # feeds = {k: v for k, v in matches}
            # self.feeds.update(feeds)

    def channel_to_toml(self, id, name):
        url = f"https://www.liveatc.net/play/{id}.pls"
        return f"""[{id}]
        name = "{name}"
        url = "{url}"
        tags = ["liveatc", "atc"]\n
        """.replace(
            "    ", ""
        )

    def save(self, output):
        with open(output, "w") as f:
            for id, name in self.feeds.items():
                toml = self.channel_to_toml(id, name)
                f.write(toml)


if __name__ == "__main__":
    liveatc = GenerateLiveATC()
    liveatc.generate(sys.argv[1])
