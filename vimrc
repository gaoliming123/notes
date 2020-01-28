" vim config for myself

inoremap kj <Esc>
inoremap KJ <Esc>
inoremap kJ <Esc>
inoremap Kj <Esc>

map <C-j> <C-W>j
map <C-h> <C-W>h
map <C-k> <C-W>k
map <C-l> <C-W>l

" gh head of line, gl end of line, gm middle of line
nnoremap gh ^
nnoremap gl $
map gm :call cursor(0, virtcol('$')/2)<CR>

" ' ` jump to the marks
" by default, ' jumps to the marked line, ` jumps to the marked line and
" column, of swap them
nnoremap ' `
nnoremap ` '
