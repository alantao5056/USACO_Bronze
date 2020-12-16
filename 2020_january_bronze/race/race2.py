def getTime(K, x):
  speedList = []
  while True:
    


def main(inputFile: str, outputFile: str):
  raceInput = open(inputFile, 'r')
  raceOutput = open(outputFile, 'w')

  K, N = [int(x) for x in raceInput.readline().strip().split()]

  for _ in range(N):
    x = int(raceInput.readline().strip())
    raceOutput.write(f'{getTime(K, x)}\n')


main('race.in', 'race.out')
