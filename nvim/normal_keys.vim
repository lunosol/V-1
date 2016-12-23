function! SingleInsert(com, count)
  let c = nr2char(getchar())
  exe "normal! ".a:com.repeat(c, a:count)."\<esc>"
endfunction

nnoremap é :<C-u>call SingleInsert('i', v:count1)<CR>
nnoremap É :<C-u>call SingleInsert('I', v:count1)<CR>
nnoremap 0é :<C-u>call SingleInsert('i', 0)<CR>
nnoremap 0É :<C-u>call SingleInsert('I', 0)<CR>
nnoremap á :<C-u>call SingleInsert('a', v:count1)<CR>
nnoremap Á :<C-u>call SingleInsert('A', v:count1)<CR>
nnoremap 0á :<C-u>call SingleInsert('a', 0)<CR>
nnoremap 0Á :<C-u>call SingleInsert('A', 0)<CR>

function! RecordQ(count)
  let c = nr2char(getchar())
  let text = ""
  while c != "ñ" && c != nr2char(255)
    let text .= c
    let c = nr2char(getchar())
  endwhile
  let @q=text.nr2char(255)
  if a:count
    call feedkeys(a:count."@q")
  endif
endfunction

nnoremap ñ :<C-u>call RecordQ(v:count1)<cr>
nnoremap 0ñ :<C-u>call RecordQ(0)<cr>

function! RecursiveQ(count)
  let c = nr2char(getchar())
  let text = ""
  while c != "ò" && c != nr2char(255)
    let text .= c
    let c = nr2char(getchar())
  endwhile
  let @q=text.nr2char(255)."@q"
  if a:count
    call feedkeys("@q")
  endif
endfunction

nnoremap ò :<C-u>call RecursiveQ(v:count1)<cr>
nnoremap 0ò :<C-u>call RecursiveQ(0)<cr>

function! PasteOver(before)
  let l:com = 'R'.(a:before ? '' : "\<right>").repeat(getreg(v:register), v:count1)."\<esc>l"
  silent exe "normal! ".l:com
endfunction

nnoremap ð :<C-u>call PasteOver(0)<cr>
nnoremap Ð :<C-u>call PasteOver(1)<cr>

function! Duplicate(type, ...) range
  let l:yank_op = g:paste_num ? 'd' : 'y'
  let l:paste_op = 'P'
  if line('.') == line('$') && l:yank_op == 'd' && a:type == 'line'
    let l:paste_op = 'p'
  endif
  if a:0  " Invoked from Visual mode, use gv command.
    silent exe "normal! gv".l:yank_op
  elseif a:type == 'line'
    silent exe "normal! '[V']".l:yank_op
  else
    silent exe "normal! `[v`]".l:yank_op
  endif

  if g:paste_num > 0
    silent exe "normal! ".g:paste_num.l:paste_op
  elseif g:paste_num == 0
    silent exe "normal! ".l:paste_op
  endif
endfunction

nnoremap ä :<C-u>let g:paste_num=v:count<cr>:set opfunc=Duplicate<cr>g@
nnoremap Ä :<C-u>let g:paste_num=v:count<cr>:set opfunc=Duplicate<cr>g@_
nnoremap 0Ä :<C-u>let g:paste_num=-1<cr>:set opfunc=Duplicate<cr>g@_
nnoremap 0ä :<C-u>let g:paste_num=-1<cr>:set opfunc=Duplicate<cr>g@

"Duplicate line after
nnoremap Ù :<C-u>exec 'norm Y'.v:count.'p'<cr>
nnoremap 0Ù dd

let g:active_reg = 0
let g:num_regs = 1
function! NextActiveRegister(BaseCommand)
  echo a:BaseCommand
  let active_reg = nr2char(g:active_reg + 97)
  let g:active_reg += 1
  if g:active_reg >= g:num_regs
    let g:active_reg = 0
  endif
  call feedkeys(a:BaseCommand.active_reg, 'i')
endfunction

nnoremap À :<C-u>call NextActiveRegister("@")<CR>
nnoremap ¢ :<C-u>call NextActiveRegister("'")<CR>
inoremap ò <C-o>:<C-u>call NextActiveRegister('<C-v><C-r>')<CR>

function! RepCharInsert(n)
  let c = nr2char(getchar())
  call feedkeys(repeat(c, a:n), 'i')
endfunction

inoremap ± <C-o>:<C-u>call RepCharInsert(10)<cr>
inoremap ² <C-o>:<C-u>call RepCharInsert(20)<cr>
inoremap ³ <C-o>:<C-u>call RepCharInsert(3)<cr>
inoremap ´ <C-o>:<C-u>call RepCharInsert(4)<cr>
inoremap µ <C-o>:<C-u>call RepCharInsert(5)<cr>
inoremap ¶ <C-o>:<C-u>call RepCharInsert(6)<cr>
inoremap · <C-o>:<C-u>call RepCharInsert(7)<cr>
inoremap ¸ <C-o>:<C-u>call RepCharInsert(8)<cr>
inoremap ¹ <C-o>:<C-u>call RepCharInsert(9)<cr>

function! InsertRange(mode)
  if a:mode == 'n'
    normal i
  endif
  let l:a = getchar()
  let l:b = getchar()
  silent exe "normal! gi\<C-v>".join(range(a, b), "\<C-v>")."\<esc>l"
endfunction

inoremap ¬ <C-o>:call InsertRange('i')<cr>
nnoremap ¬ :call InsertRange('n')<cr>

"Minor mappings:
"<M-h> for (h)ollow.
nnoremap è ^lv$hhr<space>
nnoremap <expr> È '^lv$hhr'.nr2char(getchar())

"<M-b> for (b)reak. Break a macro on a common conditional for macros
nnoremap â ^l

"<M-/> for slide
nnoremap ¯ ^lx>>

"<M-R>, or (R)eplace. Useful for replacing an entire line with another
"character.
nnoremap Ò Vr

"Mapping to ':norm' and ':%norm'
nnoremap î :norm<space>
nnoremap Î :%norm<space>
xnoremap î :norm<space>
xnoremap Î :%norm<space>
cnoremap î norm<space>
cnoremap Î %norm<space>

"Mapping reverse indent mode
inoremap <C-_> <C-o>:se ri!<cr>
