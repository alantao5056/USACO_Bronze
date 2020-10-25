import collections

def backwardShuffle(order, cows):
  newList = [-1] * len(order)
  for i in range(0, len(order)):
    newList[i] = cows[order[i] - 1]
  return newList

def performShuffle(order, cows):
  orderDict = dict(zip(order, cows))
  sortedDict = collections.OrderedDict(sorted(orderDict.items()))
  result = []
  for _, val in sortedDict.items():
    result.append(val)
  return result

def getFinalOrder(order, cows):
  shuffle1 = backwardShuffle(order, cows)
  shuffle2 = backwardShuffle(order, shuffle1)
  shuffle3 = backwardShuffle(order, shuffle2)
  return [i + '\n' for i in shuffle3]

def main(inputFile, outputFile):
  shuffleInput = open(inputFile, 'r')
  shuffleOutput = open(outputFile, 'w')
  
  N = int(shuffleInput.readline().strip())
  
  order = shuffleInput.readline().strip().split()
  order = [int(i) for i in order]
  
  cows = shuffleInput.readline().strip().split()
  
  shuffleOutput.writelines(getFinalOrder(order, cows))
  shuffleInput.close()
  shuffleOutput.close()

main('shuffle.in', 'shuffle.out')