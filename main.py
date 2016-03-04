import neovim
import subprocess
import threading
import time
import os
import sys

def setupNvim():
    nvimLauncherThread = threading.Thread(target=callNvim)
    nvimLauncherThread.start()
    time.sleep(1)
    return nvimLauncherThread

def getNvim():
    return neovim.attach("socket", path="/tmp/nvim")

def callNvim():
    if os.path.exists("/tmp/nvim"):
        os.remove("/tmp/nvim")
    os.system("$TERM -e 'bash -c ./neovim.sh'")

def welcomeMessage():
    print("Hi, welcome to V!\nUsage:\n\tv [file.v]\n\tv [file.v] [secondaryFile.txt])")

esc = chr(27)
enter = chr(13)

def main():
    args = sys.argv
    if len(args) < 2:
        welcomeMessage()
        return
    
    vFile = args[1]
    secondaryFile = ""
    if len(args) >= 4:
        secondaryFile = args[2]

    if not os.path.exists(vFile):
        fileNotFoundMessage(vFile)
        return

    if secondaryFile:
        print("We're sorry, but secondary files are not implemented yet.")

    nvimThread = setupNvim() 
    nvim = getNvim()

    with open(vFile) as source:
        for line in source:
            for char in line:
                if ord(char) < 128:
                    #print(char)
                    #raw_input()
                    #nvim.feedkeys(char, options='nt')
                    nvim.input(char)
            nvim.input(enter)

    exitString = ":q!" + enter

    for buf in nvim.buffers:
        for line in buf:
            print(line)

    #if secondaryFile:
    #   exitString = ":wq!" + enter

    nvim.input(exitString)
    

if __name__ == "__main__":
    main()
