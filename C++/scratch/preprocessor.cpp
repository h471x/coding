#include <iostream>
using namespace std;

#define test(c,v) for(int i = 1 ; i < c; ++i) cout << v[i] << endl;

int main(int argc, char* argv[]){
  test(argc, argv);
  cout << "Invoked with " << argv[0] << endl;
}
