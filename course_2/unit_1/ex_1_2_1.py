# Расстановка скобок в коде
#
# Sample Input 1:
# ([](){([])})
# Sample Output 1:
# Success
# Sample Input 2:
# ()[]}
# Sample Output 2:
# 5
# Sample Input 3:
# {{[()]]
# Sample Output 3:
# 7

def check(n):

    stack = []

    for char in n:
        if (char == '{') or (char == '['):
            stack.append(char)
        elif char == '}':
            if (len(stack) > 0) and (stack[-1] == '{'):
                stack.pop()
            else:
                stack.append(char)

        elif char == ']':
            if (len(stack) > 0) and (stack[-1] == '['):
                stack.pop()
            else:
                stack.append(char)

    if len(stack) == 0:
        return 0
    else:
        return len(n)


def main():
    # n = input()
    # check(n)

    assert check("([](){([])})") == 0
    assert check("()[]}") == 5
    assert check("{{[()]]") == 7
    assert check("{{{[][][]") == 3
    assert check("{*{{}") == 3
    assert check("[[*") == 2
    assert check("{*}") == 0
    assert check("{{") == 2
    assert check("{}") == 0
    assert check("") == 0
    assert check("}") == 1
    assert check("*{}") == 0
    assert check("{{{**[][][]") == 3

if __name__ == "__main__":
    main()