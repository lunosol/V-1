enter = chr(13)
esc = chr(27)
M_i = chr(233) 

def M_q_loop(v):
    v.set_register('q', v.recorded_text)
    command = "{}@q".format(v.pending_number)
    v.pending_number = ""
    v.recorded_text = ""
    v.nvim_instance.input(command)

def run_M_i(V):
    if len(V.pending_command) > 1:
        command = "{}i{}{}".format(V.pending_number, V.pending_command[1], esc)
        V.nvim_instance.input(command)
        V.pending_command = ""
        V.pending_number = ""

def run_M_a(V):
    if len(V.pending_command) > 1:
        command = "{}a{}{}".format(V.pending_number, V.pending_command[1], esc)
        V.nvim_instance.input(command)
        V.pending_command = ""
        V.pending_number = ""

def run_at(V):
    if len(V.pending_command) > 1:
        reg = V.get_register(V.pending_command[1])
        if reg.isdigit():
            V.pending_number = reg
        else:
            V.nvim_instance.input(V.pending_command)

        V.pending_command = ""

def run_M_L(V):
    V.nvim_instance.input("0v$")
    V.pending_number = ""
    V.pending_command = ""

def M_r_loop(v):
    v.recorded_text += "@q"
    v.set_register('q', v.recorded_text)
    command = "{}@q".format(v.pending_number)
    v.pending_number = ""
    v.recorded_text = ""
    v.nvim_instance.input(command)

M_L = chr(204)
M_a = chr(225)
M_l = chr(236)
M_q = chr(241)
M_r = chr(242)

normal_keys = [M_L, M_i, M_a, '@']
normal_functions = [run_M_L, run_M_i, run_M_a, run_at]

loop_keys = [M_q, M_r]
loop_functions = [M_q_loop, M_r_loop]

