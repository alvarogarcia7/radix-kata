# Vim -> 
#:nnoremap t :wa <bar> :!make test <CR>
init:
	uv sync --all-extras
.PHONY: init

test:
	uv run pytest .
.PHONY: test

clean:
	rm -rf test test.dSYM
.PHONY: clean

