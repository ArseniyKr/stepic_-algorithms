def sortByLastDot(inputSet):
    return list(inputSet)[-1]

countOfLines = int(input())
setList = []
for i in range(0, countOfLines):
    x1, x2 = map(int, input().split())
    linesSet = set(range(x1, x2 + 1))
    setList.append(linesSet)

setList.sort(key=sortByLastDot)

resultSet = set()

for setCurrent in setList:
    m = setList.copy()
    m.remove(setCurrent)
    listCurrent = list(setCurrent)
    for n in m:
        if listCurrent[0] in n:
            resultSet.add(listCurrent[0])

        if listCurrent[-1] in list(m):
            resultSet.add(listCurrent[-1])

resultList = list(resultSet)
resultList.sort()

print(len(resultList))

resultStr = ''
for dot in resultSet:
    resultStr += str(dot) + ' '

print(resultStr)



def coverset(n, xs):
    result = []
    sortedxs = sorted(xs,key=lambda x: x[1])
    while sortedxs:
        result.append(sortedxs[0][1])
        del sortedxs[0]
        sortedxs[:] = [x for x in sortedxs if not x[0] <= result[-1] <= x[1]]
    return (len(result),result)


def main():
    n = int(input())
    xs = []
    for i in range(n):
        xs.append(list(map(int, input().split())))
    solution = coverset(n,xs)
    print(solution[0])
    print(' '.join(map(str,solution[1])))


if __name__ == "__main__":
    main()