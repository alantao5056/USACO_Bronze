def seeIfUnique(mailBox: str, x: int, N: int) -> bool:
  mailHash = set()
  for i in range(0, N - x + 1):
    sequence = mailBox[i:i + x]
    if sequence in mailHash:
      return False
    mailHash.add(sequence)
  return True


def getValueK(mailBox: str, N: int) -> int:
  for i in range(1, N + 1):
    if seeIfUnique(mailBox, i, N):
      return i


def main(inputFile: str, outputFile: str):
  whereamiInput = open(inputFile, 'r')
  whereamiOutput = open(outputFile,  'w')

  N = int(whereamiInput.readline().strip())

  mailBox = whereamiInput.readline().strip()

  whereamiOutput.write(f'{getValueK(mailBox, N)}\n')

  whereamiInput.close()
  whereamiOutput.close()


main('whereami.in', 'whereami.out')
