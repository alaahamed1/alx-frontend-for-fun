#!/usr/bin/python3

import sys
import os

# Check if the number of arguments is less than 3 (script name + 2 arguments)
if len(sys.argv) < 3:
    # Print usage message to STDERR and exit with status 1
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

# Assign command-line arguments to variables
markdown_file = sys.argv[1]
output_file = sys.argv[2]

# Check if the Markdown file exists
if not os.path.isfile(markdown_file):
    # Print missing file message to STDERR and exit with status 1
    print(f"Missing {markdown_file}", file=sys.stderr)
    sys.exit(1)

# If all checks pass, exit with status 0
sys.exit(0)
