def getContainCows(N, pos):
  allSet = set([i for i in range(1, N + 1)])
  # finding which cows are not visited
  for p in pos:
    if p in allSet:
      allSet.remove(p)
  
  allSet = list(allSet)
  count = 0 # return this
  
  for c in allSet:
    # start search
    cur = c
    while True:
      if pos[cur - 1] == -1:
        break
      cur = pos[cur - 1]
      pos[cur - 1] = -1
      count += 1
  return N-count
      

def main(inputFile, outputFile):
  shuffleInput = open(inputFile, 'r')
  shuffleOutput = open(outputFile, 'w')
  
  N = int(shuffleInput.readline().strip())
  
  pos = list(map(int, shuffleInput.readline().strip().split()))
  
  shuffleOutput.write(str(getContainCows(N, pos)) + '\n')
  
  shuffleInput.close()
  shuffleOutput.close()
  

main('shuffle.in', 'shuffle.out')
    