def getCrossingPairs(log: str):
  logDict = {}
  count = 0
  for s in log:
    if s not in logDict:
      for key in logDict:
        logDict[key].add(s)
      logDict[s] = set()
    else:
      keys = list(logDict.keys())
      # vals = list(logDict.values())
      for i in range(0, len(keys) - 1):
        logDict[keys[i]].discard(s)
      count += len(logDict.pop(s))
  return count

def main(inputFile, outputFile):
  circlecrossInput = open(inputFile, 'r')
  circlecrossOutput = open(outputFile, 'w')
  
  log = circlecrossInput.readline().strip()
  circlecrossOutput.write(f'{getCrossingPairs(log)}\n')
  circlecrossInput.close()
  circlecrossOutput.close()

main('circlecross.in', 'circlecross.out')