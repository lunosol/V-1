enter = chr(13)
esc = chr(27)
single_i = chr(139)
as_num = chr(140)

#v_keys = [single_i, as_num]
v_keys = [single_i]
normal_keys = [single_i, as_num]

def M_q_loop(v):
    v.set_register('q', v.recorded_text)
    command = "{}@q".format(v.pending_number)
    v.pending_number = ""
    v.recorded_text = ""
    v.nvim_instance.input(command)

#def M_r_loop(v):
#    v.recorded_text += "@q"
#    v.set_register('q', v.recorded_text)
#    command = "{}@q".format(v.pending_number)
#    v.pending_number = ""
#    v.recorded_text = ""
#    v.nvim_instance.input(command)

M_q = chr(241)
M_r = chr(242)
loop_keys = [M_q]
loop_functions = [M_q_loop]

#loop_keys = [M_q, M_r]
#loop_functions = [M_q_loop, M_r_loop]

def run_single_i(V, key):
    V.nvim_instance.input("i" + key.args[0] + esc)

def run_as_number(V, key):
    number = V.get_register(key.args[0])
    V.nvim_instance.input(number)

