import re
import sys
import urllib3

BASE_FEED_URL = "https://www.liveatc.net/feedindex.php"

FEED_TYPES = ["class-b", "class-c", "class-d", "us-artcc", "canada", "international-eu", "international-oc", "international-as", "international-sa", "international-na", "international-af", "hf"]


class GenerateLiveATC():

    def __init__(self):
        self.feeds = {}

    def generate(self, output):
        self.get_feeds()
        self.save(output)

    def get_feeds(self):
        http = urllib3.PoolManager()
        for feed in FEED_TYPES:
            print(feed)
            r = http.request("GET", BASE_FEED_URL, fields={
                "type": feed,
            })
            res = r.data.decode("utf-8")
            pattern = r"""<a onClick="myDirectStream\('([^\)]*)'\)">([^<]*)<\/a>"""
            matches = re.findall(pattern, res)
            feeds = {k: v for k, v in matches}
            self.feeds.update(feeds)

    def channel_to_toml(self, id, name):
        url = f"https://www.liveatc.net/play/{id}.pls"
        return f"""[{id}]
        name = "{name}"
        url = "{url}"
        tags = ["liveatc", "atc"]\n
        """.replace("    ", "")

    def save(self, output):
        with open(output, 'w') as f:
            for id, name in self.feeds.items():
                toml = self.channel_to_toml(id, name)
                f.write(toml)


if __name__ == "__main__":
    liveatc = GenerateLiveATC()
    liveatc.generate(sys.argv[1])
