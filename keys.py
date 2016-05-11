enter = chr(13)
esc = chr(27)
M_i = chr(233) 

def M_q_loop(v):
    #Macro playback. Puts all the text between the two M_q chars, and stuffs it in 
    #'@q'. Then, if there is a pending number, it plays it back that many times.
    v.set_register('q', v.recorded_text)
    command = "{}@q".format(v.pending_number)
    v.pending_number = ""
    v.recorded_text = ""
    v.nvim_instance.input(command)

def run_M_i(V):
    #Single insert. Essentially `i<char><esc>` Takes one arbitrary key as an argument.
    if len(V.pending_command) > 1:
        command = "{}i{}{}".format(V.pending_number, V.pending_command[1], esc)
        V.nvim_instance.input(command)
        V.pending_command = ""
        V.pending_number = ""

def run_M_a(V):
    #Single append. The same as M_i, but inserts text *after* the cursor.
    if len(V.pending_command) > 1:
        command = "{}a{}{}".format(V.pending_number, V.pending_command[1], esc)
        V.nvim_instance.input(command)
        V.pending_command = ""
        V.pending_number = ""

def run_M_d(V):
    #Duplicate. Takes a 'motion' argument, yanks that motion, moves forward 
    #that motion, then (p)uts. So `<M_d>w` means (d)uplicate (w)ord.
    if len(V.pending_command) > 1:
        movement = V.pending_command[-1]
        if ord(movement) < 128:
            V.nvim_instance.input(movement)
            mode = V.get_mode()
            if mode == 'n':
                #Movement successful, exit the V command
                #full_movement = V.pending_command[1:]
                put_command = "{}P".format(V.pending_number)
                V.pending_command = ''
                V.pending_number = ''
                #V.nvim_instance.input(full_movement)
                V.nvim_instance.input(put_command)
        else:
            if movement == M_d:
                V.pending_command = ''
                V.pending_number = ''
                V.nvim_instance.input("yp")
    else:
        V.nvim_instance.input("y")
                

def run_at(V):
    #At. Playback of macros. Only overridden so that we can capture "number" macros,
    #e.g. `@a<M_q>foobar<M_q>` will playback 'foobar' 'a' times.
    if len(V.pending_command) > 1:
        reg = V.get_register(V.pending_command[1])
        if reg.isdigit():
            V.pending_number += reg
        else:
            V.nvim_instance.input(V.pending_command)

        V.pending_command = ""

def run_M_D(V):
    #Duplicate line. Literally the same as <M_d><M_d> or <M_d>y
    V.nvim_instance.input("Yp")

def run_M_L(V):
    #Select (l)ine. Originally I wanted a `dil` command (Delete In Line), but then I realised 
    #visually selecting the line is essentially the same thing.
    V.nvim_instance.input("0v$")
    V.pending_number = ""
    V.pending_command = ""

def M_r_loop(v):
    #Similar to <M_q>, but `@q` is added to the end of the macro, making it recursive.
    v.recorded_text += "@q"
    v.set_register('q', v.recorded_text)
    command = "{}@q".format(v.pending_number)
    v.pending_number = ""
    v.recorded_text = ""
    v.nvim_instance.input(command)

M_D = chr(196)
M_L = chr(204)
M_a = chr(225)
M_d = chr(228)
M_l = chr(236)
M_q = chr(241)
M_r = chr(242)

normal_keys = [M_D, M_L, M_a, M_d, M_i, '@']
normal_functions = [run_M_D, run_M_L, run_M_a, run_M_d, run_M_i, run_at]

loop_keys = [M_q, M_r]
loop_functions = [M_q_loop, M_r_loop]

