import itertools


def getCordPossible(cord, rock):
  if cord[0] == 0:
    if cord[1] == 0:
      result = [[1, 0], [0, 1]]
    elif cord[1] == 9:
      result = [[1, 9], [0, 8]]
    else:
      result = [[1, cord[1]], [0, cord[1] + 1], [0, cord[1] - 1]]
  elif cord[0] == 9:
    if cord[1] == 9:
      result = [[8, 9], [9, 8]]
    elif cord[1] == 0:
      result = [[9, 1], [8, 0]]
    else:
      result = [[8, cord[1]], [9, cord[1] + 1], [9, cord[1] - 1]]
  elif cord[1] == 0:
    result = [[1, 0], [0, 1]]
  elif cord[1] == 9:
    result = [[1, 9], [0, 8]]
  else:
    result = [[cord[0], cord[1] + 1], [cord[0], cord[1] - 1], [cord[0] + 1, cord[1]], [cord[0] - 1, cord[1]]]
  filteredRock = list(filter(rock.__ne__, result))

  # filteredResult = []
  #
  # for f in range(0, len(filteredRock)):
  #   if filteredRock[f][0] != rock[0] and filteredRock[f][1] != rock[1]:
  #     filteredResult.append(filteredRock[f])
  # return filteredRock
  return filteredRock


def isValidRoute(a, b, rock):
  if a[0] == b[0] and b[0] == rock[0]:
    if a[1] < rock[1] < b[1] or a[1] > rock[1] > b[1]:
      return False
  elif a[1] == b[1] and b[1] == rock[1]:
    if a[0] < rock[0] < b[0] or a[0] > rock[0] > b[0]:
      return False
  return True


def getRoutes(BCord, LCord, rock):
  BCordPossible = getCordPossible(BCord, rock)
  LCordPossible = getCordPossible(LCord, rock)
  combinations = list(itertools.product(BCordPossible, LCordPossible))

  return combinations


def getDistance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1]) + 1


def filterRoutes(routes, rock):
  result = []
  for r in routes:
    if isValidRoute(r[0], r[1], rock):
      result.append(r)
  return result


def buckets(BCord, LCord, rock):
  combs = getRoutes(BCord, LCord, rock)
  combs = filterRoutes(combs, rock)
  minDistance = 1000000000

  for c in combs:
    minDistance = min(minDistance, getDistance(c[0], c[1]))

  return minDistance


def main(inputFile: str, outputFile: str):
  bucketsInput = open(inputFile, 'r')
  bucketsOutput = open(outputFile, 'w')

  farmMap = []
  yAxis = 0
  BCord = []
  rock = []
  LCord = []

  for _ in range(0, 10):
    line = bucketsInput.readline().strip()
    farmMap.append(line)
    for i in range(0, len(line)):
      curCord = [yAxis, i]
      if line[i] == 'B':
        BCord = curCord
      elif line[i] == 'R':
        rock = curCord
      elif line[i] == 'L':
        LCord = curCord
    yAxis += 1
  # print(farmMap)
  # print(f'{BCord} {rock} {LCord}\n')

  bucketsOutput.write(f'{buckets(BCord, LCord, rock)}\n')

  bucketsInput.close()
  bucketsOutput.close()


main('buckets.in', 'buckets.out')
