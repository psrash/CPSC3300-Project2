# Default target to run the program with a file argument
all: run

# Run project2.py with a file argument
run:
	python3 project2.py $(FILE)

# Clean up compiled Python files
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

# Phony targets to avoid conflicts
.PHONY: all run clean