def getNumOfPalindrom(field: list) -> int:
  

def main(inputFile: str, outputFile: str):
  palpathInput = open(inputFile, 'r')
  palpathOutput = open(outputFile, 'w')
  
  N = int(palpathInput.readline().strip())
  field = []
  
  for _ in range(N):
    field.append(palpathInput.readline().strip())
  
  
  