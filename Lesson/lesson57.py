import re

text = '''
sdlfkjgkjsdgfk15889784565dslkjlkjagk12345678910
asdlfjlkjglkj 15878965457 asdfasdfasf 14785236987
16587845125
'''

print( re.findall(r"1[0-9]{10}", text) )
print( re.findall(r"1\d{10}", text) )
print( re.findall(r"1\d+", text) )
