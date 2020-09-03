import urllib3


class GenerateBase:
    """
    Base class for creating an auto-generated listing of feeds.
    """
    def __init__(self):
        self.http = urllib3.PoolManager()

    def get(self):
        """
        Main method for parsing logic
        """
        raise NotImplementedError()
