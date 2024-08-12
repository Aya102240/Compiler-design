import re
ident_pattern = r'\~[a-z0-9]+'
string_ident = input('Enter your string: ')
is_identifier = re.search(ident_pattern, string_ident)

if is_identifier:
    print(True)
else: 
    print(False)