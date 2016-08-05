import codecs
import hexdump
import os

mapping = {'\n' : '\r'}

class enc_safe_file():
    def __init__(self, file_name, utf8):
        self.enc = "utf-8" if utf8 else "CP1252"

        if os.path.exists(file_name):
            self.exists = True
            self.original_source = codecs.open(file_name, 'r', self.enc).read()
        else:
            self.exists = False

    def read(self):
        if not self.exists:
            yield []
        for line in self.original_source:
            for char in line:
                if char in mapping:
                        yield mapping[char]
                else:
                    yield char.encode("utf-8")



