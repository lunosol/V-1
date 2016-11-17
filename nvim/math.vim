function! Dec()
  let l:count = v:count - 1
  call feedkeys(l:count)
endfunction

function! Inc()
  let l:count = v:count + 1
  call feedkeys(l:count)
endfunction

nnoremap « :<C-u>call Inc()<cr>
xnoremap « :<C-u>call Inc()<cr>
nnoremap ­ :<C-u>call Dec()<cr>
xnoremap ­ :<C-u>call Dec()<cr>

