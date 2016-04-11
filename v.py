import neovim
import keys

import os
import time
import threading

class V:
    def __init__(self, secondaryFileName):
        #nvimLauncherThread = threading.Thread(target=self.__callNvim__) #Launch nvim in new thread so that V doesn't hang
        #nvimLauncherThread.start()
        #time.sleep(1)
        #self.nvimInstance = neovim.attach("socket", path="/tmp/nvim")
        os.system("whoami")
        self.nvimInstance = neovim.attach("child", argv=["/usr/bin/nvim", "--embed"])
        self.fileName = secondaryFileName

        self.pendingNumber = ""
        self.pendingCommand = None

        if self.fileName:
            self.nvimInstance.input(":e! " + secondaryFileName + chr(13))
       
    def __callNvim__(self):
        if os.path.exists("/tmp/nvim"):
            os.remove("/tmp/nvim")
        arg = "$TERM -e 'bash -c ./neovim.sh'"
        os.system(arg)
    
    def keyStroke(self, key):
        if self.pendingCommand != None:
            result = self.pendingCommand.addArg(key)

        else:
            if key.isdigit():
                self.pendingNumber += key
                
            elif key not in keys.vKeys:
                if self.pendingNumber != "":
                    self.nvimInstance.input(self.pendingNumber)
                    self.pendingNumber = ""
                self.nvimInstance.input(key)
        
            else:
                self.pendingCommand = keys.key(key, self.pendingNumber)

        if self.pendingCommand != None and self.pendingCommand.ready():
            self.pendingCommand.run(self)
            self.pendingCommand = None
                    

    def setRegister(self, register, value):
        command = ":let @{}='{}'".format(register, value)
        try:
            self.nvimInstance.command(command)
            return True
        except:
            return False

    def getMode(self):
        return self.nvimInstance.eval("mode()")

    def getRegister(self, register):
        command = ":echo @{}".format(register)
        try:
            return self.nvimInstance.command_output(command)
        except:
            return False

    def feedString(self, commands):
        for c in commands:
            self.keyStroke(c)

    def getText(self):
        for line in self.nvimInstance.buffers:
            yield line

    def cleanUp(self):
        if self.getMode() == "i":
            self.nvimInstance.input(keys.esc)

        exitCommands = ":q!" + keys.enter
        if self.fileName:
            exitCommands = ":wq!" + keys.chr(13)

        #self.nvimInstance.quit(exitCommands)
        self.nvimInstance.input(exitCommands)
