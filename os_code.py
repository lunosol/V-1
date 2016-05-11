def get_embedded_nvim_args(platform, secondary_file_path, log_file):
    if platform == "Windows":
        args = ["nvim.exe", "-i", "NONE", "-u", "NONE"]
    elif platform == "Linux":
        args = ["/usr/bin/nvim", "-i", "NONE", "-u", "NONE"]

    if log_file:
        args += ['-W', log_file]
    if secondary_file_path:
        args += [secondary_file_path]

    args += ["--embed"]

    return args

def get_socket_path(platform):
    if platform == "Windows":
        return "\\\\.\\pipe\\nvim"
    elif platform == "Linux":
        return "/tmp/nvim"

def get_external_nvim_command(platform, secondary_file_path, log_file):
    if platform == "Windows":
        #command = "START C:\\users\\jmhjr\\Desktop\\nvim-qt\\nvim-qt.exe \i NONE \u NONE {}"
        command = "START nvim-qt.exe \i NONE \u NONE {}"
    elif platform == "Linux":
        #command = "$TERM -e '/usr/bin/nvim -i NONE -u NONE {}'"
        command = "$TERM -e 'nvim -i NONE -u NONE "

    if log_file:
        command += '-W log_file '
    if secondary_file_path:
        command += "-f {} ".format(secondary_file_path)

    command += "'"

    return command
