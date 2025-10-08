# Compiler configurations
CC = gcc
CXX = g++

# Compilation flags
CFLAGS = -Wall -Wextra -std=c11
CXXFLAGS = -Wall -Wextra -std=c++11

# Output directories
BIN_DIR = bin

# Targets
.PHONY: all cpp c clean

all: cpp

cpp: $(BIN_DIR)/hello_cpp

c: $(BIN_DIR)/hello_c

$(BIN_DIR)/hello_cpp: src/hello.cpp
	mkdir -p $(BIN_DIR)
	$(CXX) $(CXXFLAGS) -o $@ $<

$(BIN_DIR)/hello_c: src/hello.c
	mkdir -p $(BIN_DIR)
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(BIN_DIR)/*
