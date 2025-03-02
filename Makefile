#	Sabyasachi Behera
#	P01 - Islands in the Stream
#	Mar 02 2025
#
#	I certify that this is my work and, where appropriate, an extension of the starter code provided
#    for the assignment.

# Compiler
CXX = g++
CXXFLAGS = -std=c++11 -Wall -Wextra -fopenmp

# Find all .cc files and create a list of executables
SOURCES := $(wildcard *.cc)
EXECUTABLES := $(SOURCES:.cc=)

# Default target: build all executables
all: $(EXECUTABLES)

# Rule to compile each .cc file into an executable
%: %.cc
	$(CXX) $(CXXFLAGS) $< -o $@

# Clean rule to remove all executables
clean:
	rm -f $(EXECUTABLES)
