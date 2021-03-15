def getDifference(a, b):
  return abs(a - b)

def getMinDistance(start, end, tpA, tpB):
  # getting distance without any kind of portal. 
  normalDistance = getDifference(start, end)
  # getting distance from tpA.
  tpADistance = getDifference(start, tpA) + getDifference(tpB, end)
  # getting distance from tpB.
  tpBDistance = getDifference(start, tpB) + getDifference(tpA, end)
  return min(normalDistance, tpADistance, tpBDistance)

def main(inputFile, outputFile):
  teleportInput = open(inputFile, 'r')
  teleportOutput = open(outputFile, 'w')
  
  line = teleportInput.readline().strip().split()
  start = int(line[0])
  end = int(line[1])
  tpA = int(line[2])
  tpB = int(line[3])
  teleportOutput.write(f'{getMinDistance(start, end, tpA, tpB)}\n')
  
  teleportInput.close()
  teleportOutput.close()

main('teleport.in', 'teleport.out')