def get_embedded_nvim_args(args):
    if args["platform"] == "Windows":
        nvim_args = ["nvim.exe", "-i", "NONE", "-u", "NONE"]
    elif args["platform"] == "Linux":
        nvim_args = ["/usr/bin/nvim", "-i", "NONE", "-u", "NONE"]

    if args["-w"]:
        nvim_args += ['-W', args["-w"]]
    if args["-f"]:
        nvim_args += [args["-f"]]
    if args["--safe"]:
        nvim_args += [args["-Z"]]

    nvim_args += ["--embed"]

    return nvim_args

def get_socket_path(args):
    if args["platform"] == "Windows":
        return "\\\\.\\pipe\\nvim"
    elif args["platform"] == "Linux":
        return "/tmp/nvim"

def get_external_nvim_command(args):
    if args["platform"] == "Windows":
        #command = "START C:\\users\\jmhjr\\Desktop\\nvim-qt\\nvim-qt.exe \i NONE \u NONE {}"
        command = "START nvim-qt.exe \i NONE \u NONE {}"
    elif args["platform"] == "Linux":
        #command = "$TERM -e '/usr/bin/nvim -i NONE -u NONE {}'"
        command = "$TERM -e 'nvim -i NONE -u NONE "

    if args["-w"]:
        command += '-W args["-w"] '
    if args["-f"]:
        command += "-f {} ".format(args["-f"])

    command += "'"

    return command
