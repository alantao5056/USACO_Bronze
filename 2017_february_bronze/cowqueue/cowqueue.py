def getMinTimeFinish(cows):
  cows = sorted(cows)
  curTime = cows[0][0] + cows[0][1]
  for i in range(1, len(cows)):
    if curTime > cows[i][0]:
      # overlapped
      curTime += cows[i][1]
    else:
      timeTakesToFinish = cows[i][0] + cows[i][1]
      curTime = timeTakesToFinish
  return curTime
    

def main(inputFile, outputFile):
  cowqueueInput = open(inputFile, 'r')
  cowqueueOutput = open(outputFile, 'w')
  
  N = int(cowqueueInput.readline().strip())
  
  cows = []
  for _ in range(N):
    line = cowqueueInput.readline().strip().split()
    cows.append([int(line[0]), int(line[1])])
  
  cowqueueOutput.write(f'{getMinTimeFinish(cows)}\n')
  cowqueueInput.close()
  cowqueueOutput.close()

main('cowqueue.in', 'cowqueue.out')