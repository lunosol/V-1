function! SingleInsert()
  let c = nr2char(getchar())
  exe "normal! ".v:count1."i".c."\<esc>"
endfunction

function! SingleAppend()
  let c = nr2char(getchar())
  exe "normal! ".v:count1."a".c."\<esc>"
endfunction

nnoremap é :<C-u>call SingleInsert()<CR>
nnoremap á :<C-u>call SingleAppend()<CR>

function! RecordQ()
  let c = nr2char(getchar())
  let text = ""
  while c != "ñ"
    let text .= c
    let c = nr2char(getchar())
  endwhile
  let @q=text
  call feedkeys(v:count1."@q")
endfunction

nnoremap ñ :<C-u>call RecordQ()<cr>

function! RecursiveQ()
  let c = nr2char(getchar())
  let text = ""
  while c != "ò"
    let text .= c
    let c = nr2char(getchar())
  endwhile
  let @q=text."@q"
  call feedkeys(v:count1."@q")
endfunction

nnoremap ò :<C-u>call RecursiveQ()<cr>

function! Duplicate()
  let motion = nr2char(getchar())
  if v:count1 == 1
    call feedkeys("y")
  else
    call feedkeys("d")
  endif
  call feedkeys(motion)
  while mode(1) != 'n'
    let motion = nr2char(getchar())
    call feedkeys(motion)
  endwhile

  call feedkeys(v:count1."P")
endfunction

nnoremap ä :<C-u>call Duplicate()<cr>
nnoremap Ä :<C-u>call Duplicate()<cr>_
