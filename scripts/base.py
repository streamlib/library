import toml

from pathlib import Path


class GenerateBase:
    """
    Base class for creating an auto-generated listing of feeds.
    """

    def __init__(self):
        self.lib_path = (Path(__file__).parents[1] / "library").resolve()

    @property
    def OUTPUT_TOML(self):
        raise NotImplementedError("Subclass must define an OUTPUT_TOML constant value")

    def get(self):
        """
        Main method for parsing logic
        """
        raise NotImplementedError("Subclass must implement feed logic in get()")

    def generate(self):
        feeds = self.get()
        print(self.lib_path / self.OUTPUT_TOML)
        with open(self.lib_path / self.OUTPUT_TOML, "w") as f:
            toml.dump(feeds, f)
