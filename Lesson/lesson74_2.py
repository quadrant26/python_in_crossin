import urllib.request, time, _thread

def get_content(i):
    id = 1764798 + i
    url = 'https://api.douban.com/v2/movie/subject/%d' % id
    try:
        d = urllib.request.urlopen(url).read()
        data.append(d)
    except:
        print("error:" , id)
    print(i, time.time() - time_start)
    print('data: ', len(data))

print( dir(_thread ) )

time_start = time.time()
data = []
for i in range(30):
    print("request movie:", i)
    _thread.start_new_thread(get_content, (i,))

input('press ENTER to exit...\n')

