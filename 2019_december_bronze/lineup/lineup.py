from itertools import permutations

def checkIfInOrder(cows, cowHash):
  for i in range(0, 8):
    if cowHash[cows[i]] == None:
      continue
    if len(cowHash[cows[i]]) == 2:
      try:
        if cows[i + 1] != cowHash[cows[i]][0] and cows[i - 1] != cowHash[cows[i]][1]:
          if cows[i + 1] != cowHash[cows[i]][1] and cows[i - 1] != cowHash[cows[i]][0]:
            return False
      except IndexError:
        return False
    else: # there is only one rule
      first = False
      try:
        # if on right side
        if cows[i + 1] == cowHash[cows[i]][0]:
          first = True
      except IndexError:
        pass
      if not first:
        #  not on right side or index error
        try:
          if cows[i - 1] != cowHash[cows[i]][0]:
            # not on left side
            return False
        except IndexError:
          # it's the first one
          return False
  return True

def getCowOrder(cowHash: dict) -> str:
  defaultOrder = [
    'Beatrice',
    'Sue',
    'Belinda',
    'Bessie',
    'Betsy',
    'Blue',
    'Bella',
    'Buttercup'
  ]

  possibleList = []

  for p in permutations(defaultOrder, 8):
    if checkIfInOrder(p, cowHash):
      possibleList.append('\n'.join(p))

  return min(x for x in possibleList if isinstance(x, str))


def main(inputFile: str, outputFile: str):
  lineupInput = open(inputFile, 'r')
  lineupOutput = open(outputFile, 'w')

  cowHash = {
    'Beatrice': None,
    'Sue': None,
    'Belinda': None,
    'Bessie': None,
    'Betsy': None,
    'Blue': None,
    'Bella': None,
    'Buttercup': None
  }

  N = int(lineupInput.readline().strip())

  for _ in range(N):
    line = lineupInput.readline().strip().split()
    if cowHash[line[0]] != None:
      cowHash[line[0]] = (cowHash[line[0]][0], line[5])
    else:
      cowHash[line[0]] = (line[5],)

  # print(cowHash)

  lineupOutput.write(getCowOrder(cowHash) + '\n')

  lineupInput.close()
  lineupOutput.close()


main('lineup.in', 'lineup.out')
