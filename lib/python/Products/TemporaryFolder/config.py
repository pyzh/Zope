from ZODB.config import BaseConfig

class TemporaryStorage(BaseConfig):
    def open(self):
        from Products.TemporaryFolder.TemporaryStorage import TemporaryStorage
        return TemporaryStorage(self.config.name)
