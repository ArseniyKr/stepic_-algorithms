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

for setIdx in range(0,  len(setList) - 1):
    resultSet = resultSet | (setList[setIdx] & setList[setIdx + 1])


resultList = list(resultSet)
resultList.sort()

print(len(resultList))

resultStr = ''
for dot in resultSet:
    resultStr += str(dot) + ' '

print(resultStr)