
def fib_digit(n):
    list = [0, 1]
    for i in range(2, n + 1):
        last_digit = (list[i-1] + list[i-2]) % 10
        list.append(last_digit)
    return list[-1]

def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()