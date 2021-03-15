def canYouGetThere(a, b, connectionHash):
  cur = a
  while True:
    if cur == b:
      return True
    if cur not in connectionHash:
      return False
    cur = connectionHash[cur]


def getConnectedToAll(connectionHash, N):
  trueList = []
  for i in range(1, N + 1):
    count = 0
    for j in range(1, N + 1):
      if i != j:
        if canYouGetThere(j, i, connectionHash):
          count += 1
    if count == N - 1:
      trueList.append(i)

  try:
    return min(trueList)
  except ValueError:
    return -1


def main(inputFile, outputFile):
  factoryInput = open(inputFile, 'r')
  factoryOutput = open(outputFile, 'w')

  N = int(factoryInput.readline().strip())
  connectionHash = {}

  for _ in range(N - 1):
    line = factoryInput.readline().strip().split()
    a, b = int(line[0]), int(line[1])
    if a in connectionHash:
      connectionHash[a] += b
    else:
      connectionHash[a] = b

  factoryOutput.write(str(getConnectedToAll(connectionHash, N)) + '\n')

  factoryInput.close()
  factoryOutput.close()


main('factory.in', 'factory.out')
