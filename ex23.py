# Strings, Bytes, and Character Encodings 
# Using file created with a list of human languages 

import sys 
script, input_encoding, error = sys.argv 

# function reads one line from languages file given 
# if-statement lets you make decisions in code 
# readline() func will return empty string when reaches end of file 
# notice loop; calling main func inside def main. 
# if-statement keeps func from looping forever (will stop if line is empty, end of txt file)
def main(language_file, encoding, errors): 
    line = language_file.readline()

    if line: 
            print_line(line, encoding, errors)
            return main(language_file, encoding, errors)

# next_lang is a string; need to call .encode to get raw bytes
# creates cooked_string var; takes raw bytes and uses .decode to string 
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf - 8")

main(languages, input_encoding, error)
