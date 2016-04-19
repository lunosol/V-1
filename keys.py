enter = chr(13)
esc = chr(27)
single_i = chr(233) 

def M_q_loop(v):
    v.set_register('q', v.recorded_text)
    command = "{}@q".format(v.pending_number)
    v.pending_number = ""
    v.recorded_text = ""
    v.nvim_instance.input(command)

def run_single_i(V):
    if len(V.pending_command) > 1:
        command = "{}i{}{}".format(V.pending_number, V.pending_command[1], esc)
        V.nvim_instance.input(command)
        V.pending_command = ""
        V.pending_number = ""


def M_r_loop(v):
    v.recorded_text += "@q"
    v.set_register('q', v.recorded_text)
    command = "{}@q".format(v.pending_number)
    v.pending_number = ""
    v.recorded_text = ""
    v.nvim_instance.input(command)

M_q = chr(241)
M_r = chr(242)

v_keys = [single_i]
normal_keys = [single_i]
normal_functions = [run_single_i]

loop_keys = [M_q, M_r]
loop_functions = [M_q_loop, M_r_loop]

