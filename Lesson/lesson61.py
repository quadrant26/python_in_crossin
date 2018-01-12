import time

strattime = time.time()
print("start: %f " % strattime)

for i in range(10):
    print(i)

endtime = time.time()
print("end: %f " % endtime)
print( "total time: %f" % (endtime - strattime) )

# 休眠
# time.sleep(secs)

print(1234)
time.sleep(3)
print(4567)
