SHELL := /bin/bash

DOT := dot
SRC := $(wildcard *.dot)
SVG := $(SRC:.dot=.svg)
PNG := $(SRC:.dot=.png)

.PHONY: all
all: $(SVG) $(PNG)

%.svg: %.dot
	$(DOT) -Tsvg -o $@ $<

%.png: %.dot
	$(DOT) -Tpng -Gdpi=150 -o $@ $<

.PHONY: clean
clean:
	rm -f $(SVG) $(PNG)
