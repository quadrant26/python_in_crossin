def printAll(**kargs):
    for k in kargs:
        print(k, ':' , kargs[k])

printAll(a=1, b=2, c=3)
printAll(x=4, y=5)

def func(x, y=5, *a, **b):
         print(x, y, a, b)

func(1)                     # 1 5 () {}
func(1, 2)                  # 1 2 () {}
func(1, 2, 3)               # 1 2 (3) {}
func(1, 2, 3, 4)            # 1 2 (3, 4) {}
func(x=1)                   # 1 5 () {}
func(x=1, y=1, a=1)     # 1 1 () {a:1}
func(x=1, y=1, a=1, b=1) # 1 1 () {a:1, b:1}
func(1, y=1)                    # 1 1 () {}
func(1, 2, 3, 4, a=1)           # 1, 2 (3, 4) {a:1}
func(1, 2, 3, 4, k=1, t=2, o=3) # 1, 2, (3, 4) {k:1. t:2, o:3}
