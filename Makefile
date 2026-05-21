#vim: nnoremap t :wa <bar> :!make t <CR>
t: test
	./test
.PHONY: t

# main: main.c
# 	gcc lib.c -o main

test: test.c 
	gcc -g test.c -o test
