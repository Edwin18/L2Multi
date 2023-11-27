# -*- makefile -*-

# definitions
SHELL         := /bin/bash
CURRPATH       = $(shell pwd)
# Color definitions
BLACK         := "\033[0;30m"
RED 		  := "\033[0;31m"
GREEN 		  := "\033[0;32m"
YELLOW 		  := "\033[0;33m"
BLUE 		  := "\033[0;34m"
MAGENTA 	  := "\033[0;35m"
CYAN 		  := "\033[0;36m"
WHITE 		  := "\033[0;37m"
RESET 		  := "\033[0m"
# definition of function
define PRINT_BOXED_MESSAGE
	@MSG="$(1)"; \
	MSG_LEN=$$(echo -n "$$MSG" | wc -m); \
	TOP_BORDER=$$(printf '━%.0s' $$(seq 1 $$((MSG_LEN + 2)))); \
	BOTTOM_BORDER=$$(printf '━%.0s' $$(seq 1 $$((MSG_LEN + 2)))); \
	EMPTY_LINE=$$(printf ' %.0s' $$(seq 1 $$((MSG_LEN + 2)))); \
	echo -e $(GREEN)"┏$$TOP_BORDER┓"$(RESET); \
	echo -e $(GREEN)"┃$$EMPTY_LINE┃"$(RESET); \
	echo -e $(GREEN)"┃" $(BLUE)"$$MSG" $(GREEN)"┃"$(RESET); \
	echo -e $(GREEN)"┃$$EMPTY_LINE┃"$(RESET); \
	echo -e $(GREEN)"┗$$BOTTOM_BORDER┛"$(RESET);
endef

# https://www.gnu.org/software/make/manual/html_node/Special-Targets.html
# https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.PHONY: clean style build

clean:
	$(call PRINT_BOXED_MESSAGE,Cleaning up *.pyc files)
	-find . | grep '.pyc$$' | xargs -I {} rm {}

style:
	$(call PRINT_BOXED_MESSAGE,PEP8 & Python styles)
	@black --line-length 120 src/ && yapf -ir src/ && isort src/

build:
	$(call PRINT_BOXED_MESSAGE,Build production version of L2Multi application)
	@pyinstaller build.spec
