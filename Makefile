SHELL := /bin/bash

.PHONY: all
all:
	@echo "Hello, attendee!"

.PHONY: clean
clean:
	rm -rf .ropeproject/
