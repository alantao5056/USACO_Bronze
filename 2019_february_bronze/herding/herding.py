def getMaxMoves(b: int, e: int, m: int) -> int:
  return max(e - b, m - e) - 1


def getMinMoves(b: int, e: int, m: int) -> int:
  if e - b == 1 and m - e == 1:
    return 0
  if e - b == 2 or m - e == 2:
    return 1
  return 2


def main(inputFile: str, outputFile: str):
  herdingInput = open(inputFile, 'r')
  herdingOutput = open(outputFile, 'w')

  b, e, m = herdingInput.readline().strip().split()
  b, e, m = int(b), int(e), int(m)

  herdingOutput.write(f'{getMinMoves(b, e, m)}\n{getMaxMoves(b, e, m)}\n')

  herdingInput.close()
  herdingOutput.close()


main('herding.in', 'herding.out')
