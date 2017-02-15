from abc import abstractmethod
from os import makedirs

from os.path import exists, split


class BaseStorage:

    @abstractmethod
    def read(self, file_name): pass

    @abstractmethod
    def write(self, data, file_name): pass


class S3Storage(BaseStorage):

    def __init__(self, s3_client):
        self.s3_client = s3_client
        super().__init__()

    def read(self, file_name):
        super().read()

    def write(self, data, file_name):
        super().write()


class FileStorage(BaseStorage):

    def _create_dir_if_needed(self, file_name):
        directory, _ =  split(file_name)
        print(directory)
        if directory and not exists(directory):
            makedirs(directory)

    def read(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()

    def write(self, data, file_name):
        self._create_dir_if_needed(file_name)
        with open(file_name, 'wb+') as file:
            file.write(data)