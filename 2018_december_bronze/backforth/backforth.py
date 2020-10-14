def getNumOfPossibilities(tank1: list, tank2: list):
  tank1Orig = tank1.copy()
  tank2Orig = tank2.copy()
  result = set()
  for a in range(0, 10):
    for b in range(0, 11):
      for c in range(0, 10):
        for d in range(0, 11):
          tank1Val = 1000
          tank1Val -= tank1[a]
          tank2.append(tank1[a])
          del tank1[a]
          
          tank1Val += tank2[b]
          tank1.append(tank2[b])
          del tank2[b]
          
          tank1Val -= tank1[c]
          tank2.append(tank1[c])
          del tank1[c]

          tank1Val += tank2[d]

          result.add(tank1Val)
          tank1 = tank1Orig.copy()
          tank2 = tank2Orig.copy()
  return len(result)
    
def main(inputFile, outputFile):
  backforthInput = open(inputFile, 'r')
  backforthOutput = open(outputFile, 'w')
  
  tank1 = backforthInput.readline().strip().split()
  tank1 = list(map(int, tank1))
  
  tank2 = backforthInput.readline().strip().split()
  tank2 = list(map(int, tank2))
  
  backforthOutput.write(str(getNumOfPossibilities(tank1, tank2)) + '\n')
  
  backforthInput.close()
  backforthOutput.close()

main('backforth.in', 'backforth.out')