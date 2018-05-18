def func(n, m):
    if n == 0:
        return m
    elif m == 0:
        return n
    elif n == m:
        return n
    elif n > m:
        temp = n % m
        return func(temp, m)
    elif m > n:
        temp = m % n
        return func(n, temp)


def main():
    n, m = map(int, input().split())
    print(func(n, m))


if __name__ == "__main__":
    main()