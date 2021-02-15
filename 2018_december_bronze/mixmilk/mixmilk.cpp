#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

class bucket {
  public:
    int store;
    int milk;
};

int main()
{
  string input;
  ifstream mixmilkInput("mixmilk.in");

  while(getline(mixmilkInput, input)) {
    string store = 0;
    int i = 0;
    while (i < input.size()) {
      if (input[i] != ' ') {
        store += input[i];
      } else {
        break;
      }
      i++;
    }
    for 
  }

  mixmilkInput.close();

  return 0;
}