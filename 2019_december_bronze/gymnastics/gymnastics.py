def compare(a: int, b: int, performance: list, K: int) -> int:
  # check which one comes before
  # and which one comes after
  if performance[0].index(a) < performance[0].index(b):
    before = a
    after = b
  else:
    before = b
    after = a
  # cycle through to see if all of one element comes before the other
  for p in range(1, K):
    if performance[p].index(before) > performance[p].index(after):
      return 0

  return 1

def getConsistantCows(performance: list, K: int, N: int) -> int:
  c = 0
  for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
      c += compare(i, j, performance, K)
  return c


def main(inputFile: str, outputFile: str):
  gymnasticsInput = open(inputFile, 'r')
  gymnasticsOutput = open(outputFile, 'w')

  K, N = gymnasticsInput.readline().strip().split()
  K, N = int(K), int(N)

  performance = []
  # print(performance)

  for _ in range(K):
    line = gymnasticsInput.readline().strip().split()
    performance.append([int(x) for x in line])

  gymnasticsOutput.write(str(getConsistantCows(performance, K, N)) + '\n')

  gymnasticsInput.close()
  gymnasticsOutput.close()


main('gymnastics.in', 'gymnastics.out')
