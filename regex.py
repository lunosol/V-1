from key_defs import *

class regex:
    def __init__(self, base):
        self.base = base
        self.search = []
        self.replace = []
        self.flags = []

    def source(self, s):
        s = s.replace("\\/", Keys.M_slash)
        l = s.split("/")
        self.add_search(l[0])
        if len(l) > 1:
            self.add_replace(l[1])
        if len(l) > 2:
            self.add_flag(l[2])


    def add_search(self, search):
        for c in search:
            if ord(c) >= 128:
                self.search += ['\\' + chr(ord(c) - 128)]
            else:
                self.search += [c]

    def add_replace(self, replace):
        for c in replace:
            if ord(c) >= 128:
                self.replace += ['\\' + chr(ord(c) - 128)]
            else:
                self.replace += [c]

    def add_flag(self, flag):
        self.flags += flag

    def get_final(self):
        return self.base + "".join(self.search) + "/" + "".join(self.replace) + "/" + "".join(self.flags) + "\r"
