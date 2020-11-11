def getRidOfNotChar(animals, char):
  for k, v in animals.items():
    if char not in v:
      del animals[k]


def getMaxYes(animals: dict, characteristics: dict):
  animalsCopy = animals.copy()
  for k, v in animals.items():
    for char in v:
      if characteristics[char]:
        getRidOfNotChar(animalsCopy, char)


def main(inputFile: str, outputFile: str):
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
