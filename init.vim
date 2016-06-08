exe 'set rtp=' . expand('$V/.config/nvim')
exe 'set rtp+=' . expand('$V/.config/nvim/after')

source plugin/surround.vim
