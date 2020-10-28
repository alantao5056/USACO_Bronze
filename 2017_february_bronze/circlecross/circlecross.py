from string import ascii_uppercase

def findPairs(alph, string):
  strSet = set()
  for s in string:
    if frozenset({alph, s}) not in strSet:
      strSet.add(frozenset({alph, s}))
    else:
      strSet.remove(frozenset({alph, s}))
  return strSet

def getCrossingPairs(log: str):
  result = set()
  for alph in ascii_uppercase:
    occurence1 = log.find(alph)
    occurence2 = log.rfind(alph)
    
    result |= findPairs(alph, log[occurence1 + 1:occurence2])
  return len(result)

def main(inputFile, outputFile):
  circlecrossInput = open(inputFile, 'r')
  circlecrossOutput = open(outputFile, 'w')
  
  log = circlecrossInput.readline().strip()
  circlecrossOutput.write(f'{getCrossingPairs(log)}\n')
  circlecrossInput.close()
  circlecrossOutput.close()

main('circlecross.in', 'circlecross.out')