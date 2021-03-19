def getWordWrap(essay: list, K: int):
  result = ''
  line = essay[0]
  lineLen = len(essay[0])
  for i in range(1, len(essay)):
    if len(essay[i]) + lineLen <= K:
      if line == '':
        line += f'{essay[i]}'
      else:
        line += f' {essay[i]}'
      lineLen += len(essay[i])
    else:
      result += line + '\n'
      line = f'{essay[i]}'
      lineLen = len(essay[i])

  return result + line + '\n'


def main(inputFile: str, outputFile: str):
  wordInput = open(inputFile, 'r')
  wordOutput = open(outputFile, 'w')

  N, K, = wordInput.readline().strip().split()
  N, K, = int(N), int(K)

  essay = wordInput.readline().strip().split()

  wordOutput.write(getWordWrap(essay, K))

  wordInput.close()
  wordOutput.close()


main('word.in', 'word.out')
