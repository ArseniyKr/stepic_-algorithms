
def fib_func(n, m):
    var = 0
    my_list = [0, 1]

    for i in range(2, m * 6):
        my_list.append((my_list[i - 1] + my_list[i - 2]) % m)
        var += 1
        if (my_list[i] == 1) and (my_list[i - 1] == 0):
            break

    return my_list[n % var]

def main():
    n, m = map(int, input().split())
    print(fib_func(n, m))


if __name__ == "__main__":
    main()