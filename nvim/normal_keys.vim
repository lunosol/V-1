function! SingleInsert()
  let c = nr2char(getchar(0))
  exe "normal! ".v:count1."i".c."\<esc>"
endfunction

function! SingleAppend()
  let c = nr2char(getchar(0))
  exe "normal! ".v:count1."a".c."\<esc>"
endfunction

nnoremap é :<C-u>call SingleInsert()<CR>
nnoremap á :<C-u>call SingleAppend()<CR>

function! RecordQ()
  let c = nr2char(getchar(0))
  let text = ""
  while c != "ñ" && c != nr2char(0)
    let text .= c
    let c = nr2char(getchar(0))
  endwhile
  let @q=text
  call feedkeys(v:count1."@q")
endfunction

nnoremap ñ :<C-u>call RecordQ()<cr>

function! RecursiveQ()
  let c = nr2char(getchar(0))
  let text = ""
  while c != "ò" && c != nr2char(0)
    let text .= c
    let c = nr2char(getchar(0))
  endwhile
  let @q=text."@q"
  call feedkeys(v:count1."@q")
endfunction

nnoremap ò :<C-u>call RecursiveQ()<cr>

function! Duplicate()
  let motion = nr2char(getchar(0))
  if v:count1 == 1
    call feedkeys("y")
  else
    call feedkeys("d")
  endif
  call feedkeys(motion)
  while mode(1) != 'n'
    let motion = nr2char(getchar(0))
    call feedkeys(motion)
  endwhile

  call feedkeys(v:count1."P")
endfunction

nnoremap ä :<C-u>call Duplicate()<cr>
nnoremap Ä :<C-u>call Duplicate()<cr>_

let g:active_reg = 0
let g:num_regs = 1
function! NextActiveRegister(BaseCommand)
  echo a:BaseCommand
  let active_reg = nr2char(g:active_reg + 97)
  let g:active_reg += 1
  if g:active_reg >= g:num_regs
    let g:active_reg = 0
  endif
  call feedkeys(a:BaseCommand.active_reg)
endfunction

nnoremap À :<C-u>call NextActiveRegister("@")<CR>
nnoremap ¢ :<C-u>call NextActiveRegister("'")<CR>
inoremap ò <C-o>:<C-u>call NextActiveRegister('<C-v><C-r>')<CR>

