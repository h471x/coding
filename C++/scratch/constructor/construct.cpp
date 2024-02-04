#include <iostream>
#include <string>
using namespace std;

class Person{
  public:
    string Name;
    int Age;

  //Here comes the constructor of Person
  Person(string name, int age){
    Name = name;
    Age = age;
  }

  //Here to recover the default constructor
  Person() = default;

  void greet(){
    cout << "Hello " << Name << " you are " << Age << " years old ! " << endl;
  }
};

int main(){
  Person Hatix = Person("Hatix", 20);
  Hatix.greet();
  Person other;
  return 0;
}
