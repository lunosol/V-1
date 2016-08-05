"Set all settings to default
set all&

"Change runtime path
exe 'set rtp-=' . expand('~/.config/nvim')
exe 'set rtp-=' . expand('~/.config/nvim/after')
exe 'set rtp+=' . expand('$V/nvim')
exe 'set rtp+=' . expand('$V/nvim/after')

"Load plugins
source nvim/plugin/surround.vim
source nvim/plugin/exchange.vim

"Source V specific source files
source nvim/.init.vim-rplugin~
source nvim/vmath.vim
source nvim/motions.vim
source nvim/normal_keys.vim
source nvim/regex.vim

"Set some settings
set noautoindent
set notimeout
set nottimeout
set nowrap

"Map our 'implicit ending' character.
nnoremap ÿ <esc>
inoremap ÿ <esc>
xnoremap ÿ <esc>
cnoremap ÿ <cr>
onoremap ÿ _
