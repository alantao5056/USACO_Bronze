def getConnectedToAll(connectionList, N):
  firstNegative = False
  firstNegativeIndex = -1
  for i in range(1, N + 1):
    if connectionList[i] == -1:
      if firstNegative:
        return -1
      firstNegative = True
      firstNegativeIndex = i
  return firstNegativeIndex


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
