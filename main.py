


def myfunc(x, y):
    a = 4 * x - y - 1
    return a


def myfunc_3(a):
    for i in range(5):
        myfunc(a[i], a[i + 2])

def myfunc_4(a):
    z = a[1] + a[2]

def main():
    a = [1, 2, 3, 4, 10]
    for _ in range(100):
        myfunc_4(a)
    for _ in range(300):
        myfunc_3(a)


if __name__ == '__main__':
    main()
