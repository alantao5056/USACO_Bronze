def findR(cows: list, N: int) -> int:
  minR = 1001
  for i in range(1, N):
    if cows[i][1] == 0:
      if cows[i - 1][1] == 1:
        minR = min(minR, cows[i][0] - cows[i - 1][0])
      if cows[i + 1][1] == 1:
        minR = min(minR, cows[i + 1][0] - cows[i][0])
  return minR


def getMinSick(cows: list, N: int) -> int:
  cows = sorted(cows)
  cows.append((1002, 0))
  cows.insert(0, (1001, 0))
  
  R = findR(cows, N)
  
  cows = [c for c in cows if c[1] == 1]

  count = 0
  
  i = 0
  while i < len(cows):
    while i < len(cows) - 1:
      if cows[i + 1][0] - cows[i][0] < R:
        i += 1
      else:
        count += 1
        break
    i += 1
  
  return count + 1


def main(inputFile: str, outputFile: str):
  socdist2Input = open(inputFile, 'r')
  socdist2Output = open(outputFile, 'w')
  
  N = int(socdist2Input.readline().strip())
  cows = []
  
  for _ in range(N):
    line = socdist2Input.readline().strip().split()
    cows.append((int(line[0]), int(line[1]),))
  
  socdist2Output.write(str(getMinSick(cows, N)) + '\n')
  
  socdist2Input.close()
  socdist2Output.close()


main('socdist2.in', 'socdist2.out')
