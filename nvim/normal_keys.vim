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
