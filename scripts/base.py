import toml

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
        Main method for parsing logic
        """
        raise NotImplementedError("Subclass must implement feed logic in get()")

    def generate(self):
        feeds = self.get()
        output = f"{self.NAME}.toml"
        with open(self.lib_path / output, "w") as f:
            toml.dump(feeds, f)
