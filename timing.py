# timing : for
def test1():
    global n
    lst = []
    for i in range(n):
        lst.append(i*i)
    return sum(lst)

# timing : while
def test2():
    global n
    i = 0
    lst = []
    while i <= n:
        lst.append(i*i)
        i += 1
    return sum(lst)

#timing : map
def test3():
    global n
    lst = range(n)
    squared = list(map(lambda x: x**2, lst))
    return sum(squared)

#timing : filter
def test4():
    global n
    lst = range(n)
    squared = list(filter(lambda x: x > 0, lst))
    return sum(squared)

if __name__=='__main__':
    while True:
        try:
            n = int(input("Please enter 'n' as size of array:\n"))
            break
        except ValueError:
            print("Try again. Enter a valid number")

    from timeit import Timer
    t1 = Timer("test1()", "from __main__ import test1")
    print("FOR LOOP:")
    print(t1.timeit())
    t2 = Timer("test2()", "from __main__ import test2")
    print("WHILE LOOP:")
    print(t2.timeit())
    t3 = Timer("test3()", "from __main__ import test3")
    print("MAP:")
    print(t3.timeit())
    t4 = Timer("test4()", "from __main__ import test4")
    print("FILTER:")
    print(t4.timeit())

    #list comprefension with if and without
    #функція генератор