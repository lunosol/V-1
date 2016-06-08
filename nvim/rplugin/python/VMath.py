from __future__ import division
import neovim 
import math

class V_math_func:
    def __init__(self, func, num_args):
        self.func = func
        self.num_args = num_args

funcs = {
'1': V_math_func(lambda l: 1, 0),
'2': V_math_func(lambda l: 2, 0),
'3': V_math_func(lambda l: 3, 0),
'4': V_math_func(lambda l: 4, 0),
'5': V_math_func(lambda l: 5, 0),
'6': V_math_func(lambda l: 6, 0),
'7': V_math_func(lambda l: 7, 0),
'8': V_math_func(lambda l: 8, 0),
'9': V_math_func(lambda l: 9, 0),
'0': V_math_func(lambda l: 0, 0),
'*': V_math_func(lambda l: l[0] * l[1], 2),
'/': V_math_func(lambda l: l[0] / l[1], 2),
'-': V_math_func(lambda l: l[0] - l[1], 2),
'+': V_math_func(lambda l: l[0] + l[1], 2),
'^': V_math_func(lambda l: l[0] ** l[1], 2),
'c': V_math_func(lambda l: int(math.ceil(l[0])), 1),
'f': V_math_func(lambda l: int(math.floor(l[0])), 1),
'r': V_math_func(lambda l: int(round(l[0])), 1),
'\n': V_math_func(lambda l: l[0], 1)        #Effectively a NOP
}

class V_math:
    def __init__(self, stack=[]):
        self.stack = stack

    def execute(self, key):
        Vfunc = funcs[key]
        args = []
        for i in range(Vfunc.num_args):
            args.append(self.pop())
        self.stack.append(Vfunc.func(args))

    def exit(self):
        for i in self.stack:
            print(i)

    def pop(self):
        return self.stack.pop() if self.stack else 0

    def peek(self):
        return self.stack[-1]

@neovim.plugin
class TestPlugin(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.V_math = V_math()

    @neovim.function("TestFunction", sync=True)
    def TestFunction(self, args):
        return 3

    @neovim.function("VMathInput", sync=True)
    def VMathInput(self, args):
        #return str(args) + str(type(args)) + str(len(args))
        self.V_math.execute(str(args[0]))

    @neovim.function("VMathPop", sync=True)
    def VMathPop(self, args):
        return self.V_math.pop()

    @neovim.function("VMathPeek", sync=True)
    def VMathPeek(self, args):
        return self.V_math.peek()

