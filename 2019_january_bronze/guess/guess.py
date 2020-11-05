def numOfYes(animals, animal, characteristics):
  count = 0
  for v in animals[animal]:
    if characteristics[v] == True:
      count += 1
  return count + 1

def getMaxYes(animals, characteristics):
  count = -1
  for k, _ in animals.items():
    count = max(count, numOfYes(animals, k, characteristics))
  return count

def main(inputFile, outputFile):
  guessInput = open(inputFile, 'r')
  guessOutput = open(outputFile, 'w')

  N = int(guessInput.readline().strip())

  animals = {}
  characteristics = {}
  
  for _ in range(N):
    line = guessInput.readline().strip().split()
    cha = set(line[2:len(line)])
    animals[line[0]] = cha
    for c in cha:
      if c in characteristics:
        characteristics[c] = False
      else:
        characteristics[c] = True

  guessOutput.write(str(getMaxYes(animals, characteristics)) + '\n')
  guessInput.close()
  guessOutput.close()

main('guess.in', 'guess.out')