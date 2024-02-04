#include <iostream>
#include <string>
using namespace std;

unsigned int Hash(string& data){
  unsigned int result(0);

  for(unsigned ch: data){
    result = ch + (result << 4) + (result << 10) - result;
  }
  return result;
}

int main(){
  string text("bengy");
  unsigned int text_hashed{ Hash(text) };
  cout << text << " hash is " << text_hashed << endl;
  return 0;
}
