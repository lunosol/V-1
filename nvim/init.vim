set all&
exe 'set rtp-=' . expand('~/.config/nvim')
exe 'set rtp-=' . expand('~/.config/nvim/after')
exe 'set rtp+=' . expand('$V/nvim')
exe 'set rtp+=' . expand('$V/nvim/after')

source nvim/plugin/surround.vim
source nvim/.init.vim-rplugin~
source nvim/vmath.vim
source nvim/motions.vim
source nvim/normal_keys.vim
source nvim/regex.vim

set noautoindent
