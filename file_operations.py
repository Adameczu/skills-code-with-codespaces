#!/usr/bin/env python3
"""
Python script demonstrating file operations in GitHub Codespaces.
This shows how to read and write files using Python.
"""

import os
from datetime import datetime

def create_sample_file(filename="sample.txt"):
    """Create a sample text file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"""GitHub Codespaces Python Demo
Created: {timestamp}

This file was created by a Python script running in GitHub Codespaces!
You can edit, run, and debug Python code right in your browser.
"""
    
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"✓ Created file: {filename}")
    return filename

def read_file(filename):
    """Read and display the contents of a file."""
    if not os.path.exists(filename):
        print(f"✗ File not found: {filename}")
        return None
    
    with open(filename, 'r') as f:
        content = f.read()
    
    print(f"\n--- Contents of {filename} ---")
    print(content)
    print("--- End of file ---\n")
    return content

def main():
    print("File Operations Demo in GitHub Codespaces")
    print("=" * 50)
    
    # Create a sample file
    filename = create_sample_file()
    
    # Read the file back
    read_file(filename)
    
    print(f"✓ Demo complete! Check the '{filename}' file in your workspace.")

if __name__ == "__main__":
    main()
