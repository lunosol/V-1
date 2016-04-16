enter = chr(13)
esc = chr(27)
singleI = chr(139)
asNum = chr(140)

vKeys = [singleI, asNum]
normal_keys = [singleI, asNum]

def M_q_loop(v):
    v.setRegister('q', v.recorded_text)
    command = "{}@q".format(v.pendingNumber)
    v.pendingNumber = ""
    v.recorded_text = ""
    v.nvimInstance.input(command)

M_q = chr(241)
loop_keys = [M_q]
loop_functions = [M_q_loop]

def runSingleI(V, key):
    V.nvimInstance.input("i" + key.args[0] + esc)

def runAsNumber(V, key):
    number = V.getRegister(key.args[0])
    V.nvimInstance.input(number)

