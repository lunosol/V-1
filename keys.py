enter = chr(13)
esc = chr(27)
singleI = chr(139)

vKeys = ['q', singleI]

def runQ(V, key):
    if key.previousInt != 0:
        #command = ":let @q='{}'".format(key.args[0])
        #V.command(command)
        V.setRegister("q", key.args[0])
        macroPlayback = str(key.previousInt) + "@q"
        V.nvimInstance.input(macroPlayback)
    else:
        V.nvimInstance.input('q')

def runSingleI(V, key):
    V.nvimInstance.input("i" + key.args[0] + esc)

#unmodified = ['\x00', '\x01', '\x02', '\x03', '\x04', '\x05', '\x06', '\x07', '\x08', 
#'\t', '\n', '\x0b', '\x0c', '\r', '\x0e', '\x0f', '\x10', '\x11', '\x12', '\x13', '\x14', 
#'\x15', '\x16', '\x17', '\x18', '\x19', '\x1a', '\x1b', '\x1c', '\x1d', '\x1e', '\x1f', 
#' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
#':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 
#'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 
#'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 
#'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
#'{', '|', '}', '~', '\x7f']

argAccepted = 1
argNotAccepted = 2
argPending = 3

class key:
    def __init__(self, key, previousInt):
        self.validKey = True

        if key == 'q':
            self.endKey = 'q'
            if previousInt == 0:
                self.argsNeeded = []
            else:
                self.argsNeeded = ["endkey"]
            self.args = []
            self.keyFunc = runQ

        elif key == singleI:
            self.endKey = ""
            self.argsNeeded = ["singleChar"]
            self.args = []
            self.keyFunc = runSingleI

        else:
            self.validKey = False

        if self.validKey:
            self.previousInt = previousInt
            self.key = key
            self.pendingArgument = ""

    def addArg(self, arg):
        numArgs = len(self.args)
        nextArgType = self.argsNeeded[numArgs]
        if nextArgType == "singleChar":
            self.args += arg
            return argAccepted
        if nextArgType == "endkey":
            if arg == self.endKey:
                self.args.append(self.pendingArgument)
                self.pendingArgument = ""
                return argAccepted
            else:
                self.pendingArgument += arg 
                return argPending

    def ready(self):
        return self.validKey and len(self.args) == len(self.argsNeeded)

    def run(self, vInstance):
        self.keyFunc(vInstance, self)
