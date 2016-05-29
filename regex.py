#'s' is a string of bytes that will be exapnded into the regex that will be
#sent to neovim. If the sequence is incomplete, it will return an empty string
#to signify that we are still in the regex.
def expand_regex(s):
    if s[-1:] not in ['\r', '\n']:
        return ""
    expanded = ""

    for c in s[1:-1]:
        if ord(c) >= 128:
            expanded += '\\' + chr(ord(c) - 128)
        else:
            expanded += c

    expanded += '\r'

    return expanded

