import codecs
import os
import re

mapping = {'\n' : '\r'}
verbose_mappings = { u"<lb>": '<', u"<rb>": '>', u"<esc>": chr(27), u"<bs>": chr(8), u"<del>": chr(127) }
ctrl_mappings = { u'[': chr(27), u'\\': chr(28), u']': chr(29), u"^": chr(30), u"_": chr(31), u"?": chr(127)}

class enc_safe_file():
    def __init__(self, file_name, utf8, verbose):
        self.enc = "utf-8" if utf8 else "latin1"

        if verbose:
            self.regex = "<esc>|<M-.>|<C-.>|<rb>|<lb>|<bs>|<del>|."
        else:
            self.regex = "."

        if os.path.exists(file_name):
            self.exists = True
            self.original_source = codecs.open(file_name, 'r', self.enc).read()
        else:
            self.exists = False

    def read(self):
        if not self.exists:
            yield []
        for com in re.findall(self.regex, self.original_source):
            yield get_encoded_command(com)

def get_encoded_command(com):
    if len(com) == 1:
        return com.encode("utf-8")

    if com in verbose_mappings:
        return verbose_mappings[com].encode("utf-8")

    if re.match("<C-.>", com):
        if com[3].isalpha():
            letter = com[3].lower()
            return chr(ord(letter) - ord('a') + 1).encode("utf-8")

        return ctrl_mappings[com[3]].encode("utf-8")

    if re.match("<M-.>", com):
        return unichr(ord(com[3]) + 128).encode("utf-8")


