import neovim
import regex

CR = chr(10)
LF = chr(13)
esc = chr(27)
M_i = chr(233)

def run_M_d_quote(V):
    reg = V.active_reg
    V.active_reg = chr(ord(reg) + 1)
    V.pending_command = ""
    V.key_stroke('"')
    V.key_stroke(reg)

def run_M_at(V):
    reg = V.active_reg
    V.active_reg = chr(ord(reg) + 1)
    V.pending_command = ""
    V.key_stroke("@")
    V.key_stroke(reg)

def run_M_i(V):
    #Single insert. Essentially `i<char><esc>` Takes one arbitrary key as an argument.
    if len(V.pending_command) > 1:
        command = "{}i{}{}".format(V.pending_number, V.pending_command[1], esc)
        V.input(command)
        V.pending_command = ""
        V.pending_number = ""

def run_M_a(V):
    #Single append. The same as M_i, but inserts text *after* the cursor.
    if len(V.pending_command) > 1:
        command = "{}a{}{}".format(V.pending_number, V.pending_command[1], esc)
        V.input(command)
        V.pending_command = ""
        V.pending_number = ""

def run_M_s(V):
    if V.pending_command[-1:] == CR:
        V.pending_command = V.pending_command[1:-1]
        reg = regex.regex(":s/")
        reg.source(V.pending_command)
        command = reg.get_final()

        V.input(command)
        V.pending_command = ""

def run_M_S(V):
    if V.pending_command[-1:] == CR:
        V.pending_command = V.pending_command[1:-1]
        reg = regex.regex(":s/")
        reg.source(V.pending_command)
        reg.add_flag('g')
        command = reg.get_final()

        V.input(command)
        V.pending_command = ""

def run_M_m(V):
    if V.pending_command[-1:] == CR:
        V.pending_command = V.pending_command[1:-1]
        reg = regex.regex(":%s/")
        reg.source(V.pending_command)
        command = reg.get_final()

        V.input(command)
        V.pending_command = ""

def run_M_M(V):
    if V.pending_command[-1:] == CR:
        V.pending_command = V.pending_command[1:-1]
        reg = regex.regex(":%s/")
        reg.source(V.pending_command)
        reg.add_flag('g')
        command = reg.get_final()

        V.input(command)
        V.pending_command = ""

def run_M_d(V):
    #Duplicate. Takes a 'motion' argument, yanks that motion, moves forward
    #that motion, then (p)uts. So `<M_d>w` means (d)uplicate (w)ord.
    if len(V.pending_command) > 1:
        movement = V.pending_command[-1]
        if ord(movement) < 128:
            V.input(movement)

            #The neovim python client has a bug, where it fails to evaluate mode if a number is pending.
            if movement.isdigit() and not movement == 0:
                mode = "no"
            else:
                mode = V.get_mode()

            if mode == 'n':
                #Movement successful, exit the V command
                #full_movement = V.pending_command[1:]
                put_command = "{}P".format(V.pending_number)
                V.pending_command = ''
                V.pending_number = ''
                #V.input(full_movement)
                V.input(put_command)
        else:
            if movement == M_d:
                V.pending_command = ''
                V.pending_number = ''
                V.input("yp")
    else:
        V.input("y")

def run_M_P(V):
    print(V.nvim_instance.current.line)
    V.pending_command = ''
    V.pending_number = ''

def run_at(V):
    #At. Playback of macros. Only overridden so that we can capture "number" macros,
    #e.g. `@a<M_q>foobar<M_q>` will playback 'foobar' 'a' times.
    if len(V.pending_command) > 1:
        reg = V.get_register(V.pending_command[1])
        if reg.isdigit():
            V.pending_number += reg
        else:
            V.input(V.pending_command)

        V.pending_command = ""

def run_M_D(V):
    #Duplicate line. Literally the same as <M_d><M_d> or <M_d>y
    command = "Y{}P".format(V.pending_number)
    V.input(command)
    V.pending_command = ''
    V.pending_number = ''

def M_r_loop(V):
    #Similar to <M_q>, but `@q` is added to the end of the macro, making it recursive.
    if V.recording:
        V.recording = False
        V.recorded_text += "@q"
        V.set_register('q', V.recorded_text)
        command = "{}@q".format(V.loop_num)
        V.loop_num = ""
        V.recorded_text = ""
        V.input(command)
    else:
        V.recording = True
        V.loop_num = V.pending_number
        V.loop_symbol = M_r

    V.pending_number = ""
    V.pending_command = ""

def M_q_loop(V):
    #Macro playback. Puts all the text between the two M_q chars, and stuffs it in
    #'@q'. Then, if there is a pending number, it plays it back that many times.
    if V.recording:
        V.recording = False
        V.set_register('q', V.recorded_text)
        command = "{}@q".format(V.loop_num)
        V.loop_num = ""
        V.recorded_text = ""
        V.input(command)
    else:
        V.recording = True
        V.loop_symbol = M_q
        V.loop_num = V.pending_number

    V.pending_number = ""
    V.pending_command = ""

def M_N_rec(V):
    if V.recording:
        V.recording = False
        V.set_register('q', V.recorded_text)
        V.recorded_text = ""
        V.input(":%norm @q\r")
    else:
        V.recording = True
        V.loop_symbol = M_N

    V.pending_number = ""
    V.pending_command = ""

def M_n_rec(V):
    if V.recording:
        V.recording = False
        V.set_register('q', V.recorded_text)
        V.recorded_text = ""
        V.input(":norm @q\r")
    else:
        V.recording = True
        V.loop_symbol = M_n

    V.pending_number = ""
    V.pending_command = ""

M_d_quote = chr(162)
M_at = chr(192)
M_D = chr(196)
M_M = chr(205)
M_N = chr(206)
M_P = chr(208)
M_S = chr(211)
M_a = chr(225)
M_d = chr(228)
M_l = chr(236)
M_m = chr(237)
M_n = chr(238)
M_q = chr(241)
M_r = chr(242)
M_s = chr(243)

normal_dict = {
M_d_quote: [run_M_d_quote, 'p'],
M_at: [run_M_at, ' '],
M_D: [run_M_D],
M_S: [run_M_S, CR],
M_M: [run_M_M, CR],
M_P: [run_M_P],
M_a: [run_M_a],
M_d: [run_M_d, M_d],
M_i: [run_M_i],
M_s: [run_M_s, CR],
M_m: [run_M_m, CR],
'@': [run_at, '"'],

M_q: [M_q_loop],
M_r: [M_r_loop],
M_n: [M_n_rec],
M_N: [M_N_rec],
}

