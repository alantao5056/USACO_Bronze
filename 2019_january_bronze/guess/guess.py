def main(inputFile, outputFile):
  guessInput = open(inputFile, 'r')
  guessOutput = open(outputFile, 'w')
  
  N = int(guessInput.readline().strip())
  
  commonCharacteristics = set()
  knowledge = {}
  
  for _ in range(N):
    line = guessInput.readline().strip().split()
    characteristics = line[2:int(line[1])]
    knowledge[line[0]] = characteristics
    commonCharacteristics |= set(characteristics)
  print(commonCharacteristics)
  print(knowledge)

main('guess.in', 'guess.out')
    