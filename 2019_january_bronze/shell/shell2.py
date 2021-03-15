def getMaxScore(guess):
  arr = [-1, 0, 0, 0]
  for g in guess:
    arr[g[0]], arr[g[1]] = arr[g[1]], arr[g[0]]
    arr[g[2]] += 1
  return max(arr)

def main(inputFile, outputFile):
  shellInput = open(inputFile, 'r')
  shellOutput = open(outputFile, 'w')
  
  N = int(shellInput.readline().strip())
  guess = []
  
  for _ in range(N):
    line = shellInput.readline().strip().split()
    guess.append([int(line[0]), int(line[1]), int(line[2])])
  
  shellOutput.write(str(getMaxScore(guess)) + '\n')
  
  shellInput.close()
  shellOutput.close()

main('shell.in', 'shell.out')