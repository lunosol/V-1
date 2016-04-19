"""Usage: 
  main.py FILE [ARGUMENTS ... ]
  main.py FILE [-d | --f=file] [ARGUMENTS ... ]

Options:
  -h --help     Show this screen.
  -d            Debug mode. Opens in a visible nvim window
  --f=FILE      Open on FILE      
"""

import v
import keys

from docopt import docopt
import neovim
import subprocess
import threading
import time
import os
import sys

def main():
    has_secondary_file = args['--f']
    external_neovim = args['-d']
    source_file = args['FILE']

    if not os.path.exists(source_file):
        fileNotFoundMessage(source_file)
        return

    vInstance = v.V(has_secondary_file, external_neovim)

    with open(source_file) as source:
        for line in source:
            for char in line:
                vInstance.keyStroke(char)

    for line in vInstance.getText():
        for char in line:
            print char

    vInstance.cleanUp()

if __name__ == "__main__":
    args = docopt(__doc__, version="V alpha 0.1")
    main()
