import re

print("\bhi")
print(r"\bhi")

text = 'Hi, I am Shirley Hilton. I am his wife.'
me = re.findall(r"\S", text)
print(me)

print(re.findall(r'i.*e', "I am Shirley Hilton. I am his wife"))

text2 = "site sea sue sweet see case sse ssee loses"
print( re.findall(r"s.*?e", text2))
print( re.findall(r"\bs\S*e\b", text2))
