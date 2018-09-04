import os
import json

from storages.storage import Storage


class FileStorage(Storage):

    def __init__(self, file_name):
        self.file_name = file_name

    def read_data(self):
        if not os.path.exists(self.file_name):
            raise StopIteration

        with open(self.file_name) as f:
            data = json.load(f)
        
        return data

    def write_data(self, data_json):
        """
        :param data_array: collection of strings that
        should be written as lines
        """
        with open(self.file_name, 'w') as f:
            json.dump(data_json, f)

    def append_data(self, data):
        """
        :param data: string
        """
        print( "Json data couldn't be added.")
