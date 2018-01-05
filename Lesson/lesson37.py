d = {"key1": "value1", "key2" : "value2"}

for key in d:
    print(key + "->" + d[key])

d['key2'] = 'new value2'
d['key3'] = 'king'

del d['key1']

for key in d:
    print(key + "->" + d[key])
