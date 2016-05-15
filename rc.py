n_maps = [
"nnoremap {} :norm ".format(chr(238)),
"nnoremap {} :%norm ".format(chr(206)),
"nnoremap H gg",
"nnoremap l G$"
]

def source(V):
    for mapping in n_maps:
        V.nvim_instance.command(mapping)
