"""Usage:
  main.py FILE [ARGUMENTS ... ]
  main.py FILE [options] [ARGUMENTS ... ]
  main.py FILE [options] [-- ARGUMENTS ... ]

Options:
  -v --version  Display version
  -h --help     Show this screen.
  -u --utf8     Read the source file in utf8 encoding. This should be considered the default, but is a flag to keep the byte count lower.
  -d            Debug mode. Opens in a visible nvim window
  -f FILE       Open on FILE
  -w FILE       Log vim keystrokes in FILE
  --safe        Do not allow shell access
"""

from __future__ import print_function

import v
import keys

from docopt import docopt
import neovim
import utf8
import subprocess
import threading
import time
import platform
import os
import sys

def main():
    has_secondary_file = args['-f']
    external_neovim = args['-d']
    source_file = args['FILE']
    args["platform"] = platform.system()
    if args["platform"] == "Darwin":
        args["platform"] = "Linux"

    if args["ARGUMENTS"][:1] == ['--']:
        args["ARGUMENTS"] = args["ARGUMENTS"][1:]

    v_instance = v.V(args)

    reg = ord('a')
    for i in args["ARGUMENTS"]:
        v_instance.set_register(chr(reg), i)
        reg += 1

    v_instance.set_register('z', os.path.abspath(source_file))

    source = utf8.enc_safe_file(source_file, args["--utf8"])

    if not source.exists():
        print("Error:\nFile: {} not found.".format(source_file), file=sys.stderr)
        return

    for char in source.read():
        v_instance.key_stroke(char)

    v_instance.clean_up()

    for line in v_instance.get_text():
        for char in line:
            print(char)

    v_instance.close()


if __name__ == "__main__":
    args = docopt(__doc__, version="Alpha 0.1")
    main()
