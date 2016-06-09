function Push()
  echo VMathPush(v:count)
endfunction

function Peek()
  let n = VMathPeek()
  call feedkeys(string(n))
endfunction

function Pop()
  let n = VMathPop()
  call feedkeys(string(n))
endfunction

nnoremap <space> :<C-u>call Push()<CR>
nnoremap z :<C-u>call Peek()<CR>
nnoremap Z :<C-u>call Pop()<CR>
