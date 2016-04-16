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
        if secondaryFileName:
            self.nvimInstance = neovim.attach("child", argv=["/usr/bin/nvim", secondaryFileName, "--embed"])
        else:
            self.nvimInstance = neovim.attach("child", argv=["/usr/bin/nvim", "--embed"])

        self.fileName = secondaryFileName

        self.pendingNumber = ""
        self.recorded_text = ""
        self.loop_symbol = ""
        self.recording = False
        self.pendingCommand = None

    def __callNvim__(self):
        if os.path.exists("/tmp/nvim"):
            os.remove("/tmp/nvim")
        arg = "$TERM -e 'bash -c ./neovim.sh'"
        os.system(arg)
    
    def keyStroke(self, key):
        if self.recording:
            if key == self.loop_symbol:
                self.recording = False
                function_index = keys.loop_keys.index(key)
                keys.loop_functions[function_index](self)
                
            else:
                self.recorded_text += key
        elif key.isdigit():
            self.pendingNumber += key
        elif key in keys.loop_keys:
            self.recording = True
            self.loop_symbol = key
        elif key in keys.normal_keys:
            keys.function_list[key](self)
        else:
            self.nvimInstance.input(self.pendingNumber + key)
            self.pendingNumber = ""

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

    def getText(self):
        for line in self.nvimInstance.buffers:
            yield line

    def cleanUp(self):
        if self.getMode() == "i":
            self.nvimInstance.input(keys.esc)

        exitCommands = ":q!" + keys.enter
        if self.fileName:
            exitCommands = ":wq!" + keys.enter

        #self.nvimInstance.quit(exitCommands)
        self.nvimInstance.input(exitCommands)
