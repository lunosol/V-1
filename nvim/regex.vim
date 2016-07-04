function! Search(com)
  let c = getchar()
  let command = ""
  while c != 13
    if c > 128
      let command .= "\\".nr2char(c - 128)
    else
      let command .= nr2char(c)
    endif
    let c = getchar()
  endwhile
  exe "normal! ".a:com.command."\<CR>"
endfunction

nnoremap / :<C-u>call Search("/")<CR>
nnoremap ? :<C-u>call Search("?")<CR>
