def getNumOfPalindrom(field: list) -> int:
  pass

def main(inputFile: str, outputFile: str):
  palpathInput = open(inputFile, 'r')
  palpathOutput = open(outputFile, 'w')

  N = int(palpathInput.readline().strip())
  field = []

  for _ in range(N):
    field.append(palpathInput.readline().strip())

  palpathOutput.write(f'{getNumOfPalindrom(field)}\n')

main('palpath.in', 'palpath.out')