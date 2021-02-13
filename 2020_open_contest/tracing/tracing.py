def getMinMaxK(logs: list, infectCows: str, N: int, T: int):
  for c in range(0, N):
    for k in range(0, N):
      curInfect = [0 for _ in range(N)]
      curInfect[c] = 1
      KCows = [0 for _ in range(N)]
      for i in range(0, T):
        a = curInfect[logs[i][1] - 1]
        b = curInfect[logs[i][2] - 1]
        if (a == 1 or b == 1) and KCows[logs[i][1] - 1] < k and KCows[logs[i][2] - 1] < k:
          curInfect[logs[i][1] - 1] = 1
          curInfect[logs[i][2] - 1] = 1
        if a == 1:
          KCows[logs[i][1] - 1] += 1
        if b == 1:
          KCows[logs[i][2] - 1] += 1

def main(inputFile: str, outputFile: str):
  tracingInput = open(inputFile, 'r')
  tracingOutput = open(outputFile, 'w')

  N, T = tracingInput.readline().strip().split()
  N, T = int(N), int(T)

  infectCows = tracingInput.readline().strip()
  logs = []

  for _ in range(T):
    line = tracingInput.readline().strip().split()
    logs.append([int(line[0]), int(line[1]), int(line[2])])
  
  getMinMaxK(sorted(logs), infectCows, N, T)
    
main('tracing.in', 'tracing.out')