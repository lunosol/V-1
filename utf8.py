import codecs
import os

mapping = {}

class enc_safe_file():
    def __init__(self, file_name, utf8):
        self.enc = "utf-8" if utf8 else "latin1"
        self.file_name = file_name

        if os.path.exists(file_name):
            self.file = codecs.open(file_name, 'r', self.enc)
        else:
            self.file = None

    def read(self):
        if self.file == None:
            yield []
        for line in self.file:
            for char in line:
                if char in mapping:
                        yield mapping[char]
                else:
                    yield char.encode("latin1")

    def exists(self):
        return self.file != None
