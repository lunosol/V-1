nnoremap <M-j> :<C-u>call StraightDown('n')<cr>
nnoremap <M-k> :<C-u>call StraightUp('n')<cr>

xnoremap <M-j> :<C-u>call StraightDown('v')<cr>
xnoremap <M-k> :<C-u>call StraightUp('v')<cr>

onoremap <M-j> :<C-u>call StraightDown('o')<cr>
onoremap <M-k> :<C-u>call StraightUp('o')<cr>

nnoremap L G$
xnoremap H gg
xnoremap L G$

"Execute a motion on the 'next' text object
onoremap an :<c-u>call <SID>NextTextObject('a')<cr>
xnoremap an :<c-u>call <SID>NextTextObject('a')<cr>
onoremap in :<c-u>call <SID>NextTextObject('i')<cr>
xnoremap in :<c-u>call <SID>NextTextObject('i')<cr>
onoremap al :<c-u>call <SID>PreviousTextObject('a')<cr>
xnoremap al :<c-u>call <SID>PreviousTextObject('a')<cr>
onoremap il :<c-u>call <SID>PreviousTextObject('i')<cr>
xnoremap il :<c-u>call <SID>PreviousTextObject('i')<cr>

function! s:NextTextObject(motion)
  let c = nr2char(getchar())
  exe "normal! "v:count1."f".c."v".a:motion.c
endfunction

function! s:PreviousTextObject(motion)
  let c = nr2char(getchar())
  exe "normal! "v:count1."F".c."v".a:motion.c
endfunction

function! StraightDown(mode)
  let line=line('.')
  let end=line('$')
  if a:mode == 'v'
    exe "normal gv"
  elseif a:mode == 'o'
    exe "normal \<C-v>"
  endif
  exe "normal ".eval(end-line)."j"
endfunction

function! StraightUp(mode)
  let line=line('.')
  if a:mode == 'v'
    exe "normal gv"
  elseif a:mode == 'o'
    exe "normal \<C-v>"
  endif
  exe "normal ".eval(line-1)."k"
endfunction
