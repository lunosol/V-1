exe 'set rtp=' . expand('$V/.config/nvim')
exe 'set rtp+=' . expand('$V/.config/nvim/after')

source .nvim/plugin/surround.vim

set noautoindent

nnoremap H gg
nnoremap L G$
xnoremap H gg
xnoremap L G$

onoremap J <C-v>j
onoremap K <C-v>k

vnoremap > >gv
vnoremap < <gv

onoremap an :<c-u>call <SID>NextTextObject('a')<cr>
xnoremap an :<c-u>call <SID>NextTextObject('a')<cr>
onoremap in :<c-u>call <SID>NextTextObject('i')<cr>
xnoremap in :<c-u>call <SID>NextTextObject('i')<cr>

nnoremap <CM-b> "_d
vnoremap <CM-b> "_d

nnoremap <CM-d> dd

vnoremap v 0o$h

function! s:NextTextObject(motion)
  echo
  let c = nr2char(getchar())
  exe "normal! f".c."v".a:motion.c
endfunction
