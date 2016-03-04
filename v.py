import neovim
import literals

import os
import time
import threading

class V:
    def __init__(self, secondaryFileName):
        nvimLauncherThread = threading.Thread(target=self.__callNvim__) #Launch nvim in new thread so that V doesn't hang
        nvimLauncherThread.start()
        time.sleep(1)
        self.nvimInstance = neovim.attach("socket", path="/tmp/nvim")
        self.fileName = secondaryFileName

        if self.fileName:
            self.nvimInstance.input(":e! " + secondaryFileName + chr(13))
       
    def __callNvim__(self):
        if os.path.exists("/tmp/nvim"):
            os.remove("/tmp/nvim")
        arg = "$TERM -e 'bash -c ./neovim.sh'"
        os.system(arg)
    
    def keyStroke(self, key):
        #Add more parsing
        self.nvimInstance.input(key)

    def feedString(self, commands):
        for c in commands:
            self.keyStroke(c)

    def getText(self):
        for line in self.nvimInstance.buffers:
            yield line

    def cleanUp(self):
        exitCommands = ":q!" + literals.enter
        if self.fileName:
            exitCommands = ":wq!" + literals.chr(13)

        self.nvimInstance.input(exitCommands)
