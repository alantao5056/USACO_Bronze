def getNumOfPossibilities(tank1, tank2):
  return 0

def main(inputFile, outputFile):
  backforthInput = open(inputFile, 'r')
  backforthOutput = open(outputFile, 'w')
  
  tank1 = backforthInput.readline().strip().split()
  tank1 = list(map(int, tank1))
  
  tank2 = backforthInput.readline().strip().split()
  tank2 = list(map(int, tank2))
  
  backforthOutput.write(str(getNumOfPossibilities(tank1, tank2)) + '\n')