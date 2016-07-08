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

