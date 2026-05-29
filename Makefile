# Vim -> 
#:nnoremap t :wa <bar> :!make t <CR>
t: test
	./test
.PHONY: t

# main: main.c
# 	gcc lib.c -o main

test: test.c lib.h log/log.c log/log.h
	gcc -g test.c log/log.c -o test -I log/ 

