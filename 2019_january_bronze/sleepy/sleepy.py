def numOfInsert(arr):
  count = 1
  for i in range(len(arr) - 1, 0, -1):
    if arr[i] > arr[i - 1]:
      count += 1
    else:
      break
  return len(arr) - count

def main(inputFile, outputFile):
  sleepyInput = open(inputFile, 'r')
  sleepyOutput = open(outputFile, 'w')
  
  N = int(sleepyInput.readline().strip())
  
  arr = sleepyInput.readline().strip().split()
  arr = [int(e) for e in arr]
  
  sleepyOutput.write(str(numOfInsert(arr)) + '\n')
  
  sleepyInput.close()
  sleepyOutput.close()

main('sleepy.in', 'sleepy.out')
