from queue import PriorityQueue
import operator

class Cow():
  def __init__(self, t, w, p, i):
    self.start = t
    self.wait = w
    self.priority = p
    self.index = i

def getMaxWaiting(cows: list, N: int) -> int:
  waiting = PriorityQueue()
  waiting.put((cows[0].priority, cows[0]))
  cowCount = 1
  t = cows[0].start
  
  while True:
    if not waiting.empty():
      eatingCow = waiting.get()[1]
      t += eatingCow.wait
      for i in range(eatingCow.index + 1, N):
        curCowStart = cows[i].start
        if curCowStart > t:
          break
        waiting.put((cows[i].priority, cows[i]))
        cowCount += 1
    elif cowCount == N:
      return "finish"
    else:
      waiting.put((cows[cowCount - 1].priority, cows[cowCount - 1]))

def main(inputFile: str, outputFile: str):
  convention2Input = open(inputFile, 'r')
  convention2Output = open(outputFile, 'w')
  
  N = int(convention2Input.readline().strip())
  
  cows = []
  for i in range(N):
    t, w = convention2Input.readline().strip().split()
    
    cows.append(Cow(int(t), int(w), i+1, 0))
  
  # print(cows)
  sortedCows = sorted(cows, key=operator.attrgetter('start'))
  for i in range(N):
    sortedCows[i].index = i
  getMaxWaiting(sortedCows, N)

main('convention2.in', 'convention2.out')