import urllib.request, time

# dir(urllib.request.urlopen)

time_start = time.time()
data = []
for i in range(30):
    print('request movie:', i)
    id = 1764802 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    try:
        lib = urllib.request.urlopen(url)
        d = lib.read()
    except:
        print("error: ", id)
    data.append(d)
    print(i, time.time() - time_start)

print(len(data))
