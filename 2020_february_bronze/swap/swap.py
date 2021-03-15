def getOrderCows(N, K, A1, A2, B1, B2):
  curStr = [x for x in range(1, N + 1)]
  steps = []
  origCurStr = curStr.copy()
  pattern = 0
  for i in range(K):
    curStr[A1-1:A2] = reversed(curStr[A1-1:A2])
    curStr[B1-1:B2] = reversed(curStr[B1-1:B2])
    steps.append(curStr.copy())
    if curStr == origCurStr:
      pattern = i
      break

  return steps[K % (pattern + 1) - 1]


def main(inputFile, outputFile):
  swapInput = open(inputFile, 'r')
  swapOutput = open(outputFile, 'w')

  N, K = swapInput.readline().strip().split()

  N, K = int(N), int(K)

  A1, A2 = swapInput.readline().strip().split()
  B1, B2 = swapInput.readline().strip().split()

  A1, A2, B1, B2 = int(A1), int(A2), int(B1), int(B2)

  swapOutput.write(''.join([str(num) + '\n' for num in getOrderCows(N, K, A1, A2, B1, B2)]))

  swapInput.close()
  swapOutput.close()


main('swap.in', 'swap.out')
