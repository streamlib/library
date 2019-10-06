import re
import sys
import unicodedata
import urllib3
import uuid

RADIO_DB_URL = "https://fred181.gitlab.io/devuandog/Misc/radiodb"

SEEN_IDS = set()

class GenerateRadioDB():

    def generate(self, output):
        self.get_channels()
        self.save(output)

    def get_channels(self):
        http = urllib3.PoolManager()
        r = http.request("GET", RADIO_DB_URL)
        res = r.data.decode("utf-8")
        self.channels = [line.strip() for line in res.split("\n") if line]

    def channel_to_toml(self, line):
        url, name, tag = line.split("|")

        id = ''.join(e for e in name if e.isalnum()).lower()
        id = unicodedata.normalize('NFKD', id).encode('ascii','ignore').decode("ascii")
        if not id or id in SEEN_IDS:
            id += "-" + str(uuid.uuid4().hex)
        SEEN_IDS.add(id)

        name = name.replace('"', '')
        url = url.split("?")[0].split(";")[0]
        tag = tag.lower().replace(" ", "-")

        return f"""[{id}]
        name = "{name}"
        url = "{url}"
        tags = ["{tag}"]\n
        """.replace("    ", "")

    def save(self, output):
        with open(output, 'w') as f:
            for chan in self.channels:
                try:
                    toml = self.channel_to_toml(chan)
                    f.write(toml)
                except Exception as e:
                    print(f"error {e} on {chan}")


if __name__ == "__main__":
    radiodb = GenerateRadioDB()
    radiodb.generate(sys.argv[1])
