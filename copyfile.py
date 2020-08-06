#!/usr/bin/env python3
'''
Filename: copyfile.py
Author: Nahia Akter
Student no.: 301106956
Description: Copies the source file content to the specified destination
'''

infile = input("Enter the source file name: ")
outfile = input("Enter the destination file name: ")

source_file = open(infile, "r");
target_file = open(outfile, "w");

content = source_file.read();
target_file.write(content);

print("The source file is successfully copied to destination file")
