enter = chr(13)
esc = chr(27)
singleI = chr(139)
asNum = chr(140)

vKeys = ['q', singleI, asNum]

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

def runAsNumber(V, key):
    number = V.getRegister(key.args[0])
    V.nvimInstance.input(number)

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

        elif key == asNum:
            self.endKey = ""
            self.argsNeeded = ["text"]
            self.args = []
            self.keyFunc = runAsNum

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
            returnVal = argAccepted
        elif nextArgType == "text":
            if len(arg) == 2:
                if arg[0] == '"' and arg[1].isalpha():
                    returnVal = argAccepted
            elif len(arg) < 2:
                returnVal = argPending
            else:
                returnVal = argNotAccepted
        elif nextArgType == "endkey":
            if arg == self.endKey:
                returnVal = argAccepted
            else:
                returnVal = argPending

        if returnVal == argAccepted:
            self.args.append(self.pendingArgument)
            self.pendingArgument = ""
        elif returnVal == argPending:
            self.pendingArgument += arg
            
        return returnVal

    def ready(self):
        return self.validKey and len(self.args) == len(self.argsNeeded)

    def run(self, vInstance):
        self.keyFunc(vInstance, self)
