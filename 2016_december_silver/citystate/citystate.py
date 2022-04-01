def main(inputFile, outputFile):
  citystateInput = open(inputFile, 'r')
  citystateOutput = open(outputFile, 'w')
  
  N = int(citystateInput.readline().strip())
  
  cityState = {}
  
  count = 0
  
  for _ in range(N):
    city, state = citystateInput.readline().strip().split()
    city = city[0:2]
    
    if city in cityState and state in cityState[city]:
      if len(cityState[city]) == 1:
        del cityState[city]
      else:
        cityState[city].remove(state)
      count += 1
    else:
      if state in cityState:
        cityState[state].add(city)
      else:
        cityState[state] = set([city])
  
  citystateOutput.write(str(count) + '\n')
  
  citystateInput.close()
  citystateOutput.close()


main('citystate.in', 'citystate.out')
