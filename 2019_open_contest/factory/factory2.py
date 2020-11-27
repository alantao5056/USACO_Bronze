def getConnectedToAll(connectionList, N):
  negativeOneCount = connectionList.count(-1)
  if negativeOneCount == 2:
    for i in range(1, len(connectionList)):
      if connectionList[i] == -1:
        return i
  else:
    return -1


def main(inputFile, outputFile):
  factoryInput = open(inputFile, 'r')
  factoryOutput = open(outputFile, 'w')

  N = int(factoryInput.readline().strip())
  connectionList = [-1] * (N + 1)

  for _ in range(N - 1):
    line = factoryInput.readline().strip().split()
    a, b = int(line[0]), int(line[1])
    connectionList[a] = b
  # print(connectionList)

  factoryOutput.write(str(getConnectedToAll(connectionList, N)) + '\n')

  factoryInput.close()
  factoryOutput.close()


main('factory.in', 'factory.out')
