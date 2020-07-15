## 1324. Print Words Vertically
- `String.stripe()`method removes the characters specified at the beginning and end of a string
(either a space or a newline by default) or a sequence of characters.

- `String.rstripe()` method removes characters from the right based on the argument 
(a string specifying the set of characters to be removed).


## 468. Validate IP Address
- Check if the string has one specific character: `if ':' in s`

- Regular expression operation `re`. 

    Check if the character is in '0'-'9' or 'a'-'z' or 'A'-'Z': `re.fullmatch(r"^[0-9a-fA-F]$", c or "") is not None`
   
    [RE Cheat Sheet](http://web.mit.edu/hackl/www/lab/turkshop/slides/regex-cheatsheet.pdf)
    
- IP address package: `from ipaddress import ip_address, IPv6Address`


## 151. Reverse Words in a String
- To reverse a string. 

    `return " ".join(s.split()[::-1])`  
    
    The `join()` string method returns a string by joining all the elements of an iterable, separated by a string separator.
    
    `list[::-1]`can iterate reverse the list.
    
    
