# Learn Python 3 the Hard Way

Intro/review of basic Python 3 following the book LPTHW by Zed Shaw.

## Syntax notes:

`# comment`

`print(" ")` prints text inside quotes

- Use triple single quotes ''' to print multiple lines at once
- Can do math inside quotes, use comma to separate from string
- Use `{ }` to embed variables in string, using f first

`print(f"words {var} more words)`

`\n` new line

`\t` tab

`float()` numbers with decimal

`.format()` concatenate elements within a string, uses value stored in variable

```sh
str = "We are learning {} programming language."
print(str.format("Python"))
```

- Use `{}` to define multiple variables
- `.format(\*<variable>)` can use to apply a list to a format sring

`input()` prompts user

`argv` argument, holds values until they are "unpacked"

- need to call argument to run program
- syntax: script, arg1, arg2 = argv

`open()` opens file

- note filename inside (), use 'w' to write/replace text in file
- use 'a' to add text to end of file
  -'r' is default, opens file in read mode

`.read()` reads file with no parameters

`.close()` closes file and frees up memory when file no longer needed

`len()` returns length (bytes) of string

`def` function

- syntax: `def func_name():`
- colon at end allows for tab on next line, part of function

`.seek()` returns file to first byte (beginning)

`.readline()` reads a line of file and returns in form of string

- takes parameter `n` to specify max number of bytes that will be read
- does not read more than one line, even if `n` exceeds length of line

`rewind()` returns file to beginning after it has been read in program

- works seame as seek()

```python
import sys
script, <arg1>, <arg2> = sys.argv

if <condition>:
    <function>
    return function
    # def is not used, func is coded directly
```

`.encode()` use to encode strings to bytes

`.decode()` use to decode bytes to strings

`.split()` returns a list of strings after breaking the given string by specified operator

- syntax: `str.split(separator,maxsplit)`
- if no separator is given, will split at every blank space

`sorted()` sorts any sequence and returns a list with elements in sorted manner

- does not modify original sequence
- syntax: `sorted(sequence, key, reverse)`
- key is optional, a function that would be basis of sort comparison
- reverse is optional, if set to true, sequence would be sorted in reverse (descending) order
- reverse is set to false as default

`.pop()` removes and returns last value from list or given index value

- index is optional, value is popped out and removed
- if index is not given, then last element is popped out and removed
- returns last value or given index value from list

`""" """` triple double quotes (no print) is documentation comments

Importing file to Python and run functions - use: `from <file name> import \*`

- eliminates having to type file name before running every function
