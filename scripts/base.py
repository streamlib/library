import toml

from collections import OrderedDict
from pathlib import Path


class GenerateBase:
    """
    Base class for creating an auto-generated listing of feeds.
    """

    def __init__(self):
        self.lib_path = (Path(__file__).parents[1] / "library").resolve()

    @property
    def NAME(self):
        raise NotImplementedError("Subclass must define a canonical constant value NAME")

    def get(self):
        """
        Main method for parsing logic, must return a dictionary of feeds. e.g.
        {
            "abc": {
                "url": "http://example.com/abc.pls"
            },
            "def": {
                "url": "http://example.com/dev.pls"
                "description": "def feed description"
            }
        }
        For more details see the
        """
        raise NotImplementedError("Subclass must implement feed logic in get()")

    def validate(self, feeds):
        if not isinstance(feeds, dict):
            raise Exception("Feeds return type must be a dictionary")
        for k, v in feeds.items():
            if not isinstance(v, dict):
                raise Exception(f"Feed name {k} value must be a dictionary")
            if not v.get("url"):
                raise Exception(f"Feed name {k} must have a valid URL")

    def generate(self):
        feeds = self.get()
        self.validate(feeds)
        output = f"{self.NAME}.toml"
        with open(self.lib_path / output, "w") as f:
            toml.dump(feeds, f)
