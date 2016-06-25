set all&
exe 'set rtp-=' . expand('~/.config/nvim')
exe 'set rtp-=' . expand('~/.config/nvim/after')
exe 'set rtp+=' . expand('$V/nvim')
exe 'set rtp+=' . expand('$V/nvim/after')

source nvim/plugin/surround.vim
source nvim/.init.vim-rplugin~
source nvim/vmath.vim
source nvim/motions.vim

set noautoindent

onoremap J <C-v>j
onoremap K <C-v>k

vnoremap > >gv
vnoremap < <gv

nnoremap <CM-b> "_d
vnoremap <CM-b> "_d

nnoremap <CM-d> dd

vnoremap v 0o$h
