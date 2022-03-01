import json

class Store:
    def load_from_file(self, filepath):
        print("loading...", filepath)
        with open(filepath, 'r') as fileObj:
            return json.load(fileObj)

    def __init__(self):
        self.allowed_words = self.load_from_file('./word-files/allowed-words.json')
        self.actual_words = self.load_from_file('./word-files/words.json')
