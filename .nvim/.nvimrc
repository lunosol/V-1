<<<<<<< HEAD
nnoremap <M-n> :norm<space>
nnoremap <M-N> :%norm<space>
=======
>>>>>>> d76173309cb79fba5dfa9e388dfce9d7e3cd0031
nnoremap H gg
nnoremap L G$

onoremap J <C-v>j
onoremap K <C-v>k
<<<<<<< HEAD

onoremap an :<c-u>call <SID>NextTextObject('a')<cr>
xnoremap an :<c-u>call <SID>NextTextObject('a')<cr>
onoremap in :<c-u>call <SID>NextTextObject('i')<cr>
xnoremap in :<c-u>call <SID>NextTextObject('i')<cr>

function! s:NextTextObject(motion)
  echo
  let c = nr2char(getchar())
  exe "normal! f".c."v".a:motion.c
endfunction
=======
>>>>>>> d76173309cb79fba5dfa9e388dfce9d7e3cd0031
