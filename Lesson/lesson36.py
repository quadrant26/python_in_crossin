try:
    f = open('non-exist.txt')
    print('file opened!')
    f.close()
except:
    print('file not exists')

print('Done')
