import re
import sys
import urllib3

CAMS_SEARCH_URL = "https://www.ayalonhw.co.il/%D7%9E%D7%A6%D7%9C%D7%9E%D7%95%D7%AA-%D7%91%D7%A9%D7%99%D7%93%D7%95%D7%A8-%D7%97%D7%99/"


class GenerateILCams:
    def generate(self, output):
        self.get_channels()
        self.save(output)

    def get_channels(self):
        http = urllib3.PoolManager()
        r = http.request("GET", CAMS_SEARCH_URL)
        res = r.data.decode("utf-8")
        pattern = r"https://5e0da72d486c5.streamlock.net:8443/ayalon/([a-zA-Z0-9\-\_]*).stream/playlist.m3u8"
        matches = re.findall(pattern, res)
        self.channels = matches

    def channel_to_toml(self, name):
        url = f"https://5e0da72d486c5.streamlock.net:8443/ayalon/{name}.stream/playlist.m3u8"
        return f"""[{name.lower()}]
        url = "{url}"
        tags = ["roadcams", "israel", "ayalon"]\n
        """.replace(
            "    ", ""
        )

    def save(self, output):
        with open(output, "w") as f:
            for chan in self.channels:
                toml = self.channel_to_toml(chan)
                f.write(toml)


if __name__ == "__main__":
    ilcams = GenerateILCams()
    ilcams.generate(sys.argv[1])
