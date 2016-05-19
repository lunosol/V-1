"""Usage: 
  main.py FILE [ARGUMENTS ... ]
  main.py FILE [options] [ARGUMENTS ... ]
  main.py FILE [ARGUMENTS ... ] [options]

Options:
  -h --help     Show this screen.
  -d            Debug mode. Opens in a visible nvim window
  -f FILE       Open on FILE      
  -w FILE       Log vim keystrokes in FILE
  --safe        Do not allow shell access
"""

import v
import keys

from docopt import docopt
import neovim
import rc
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

    if not os.path.exists(source_file):
        file_not_found_message(source_file)
        return

    v_instance = v.V(args)

    rc.source(v_instance)

    reg = ord('a')
    for i in args["ARGUMENTS"]:
        v_instance.set_register(chr(reg), i)
        reg += 1

    with open(source_file) as source:
        for line in source:
            for char in line:
                v_instance.key_stroke(char)

    v_instance.clean_up()

    for line in v_instance.get_text():
        for char in line:
            print char

    v_instance.close()


if __name__ == "__main__":
    args = docopt(__doc__, version="V alpha 0.1")
    main()
