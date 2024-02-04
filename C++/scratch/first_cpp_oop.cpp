#include <iostream>
#include <string>
using namespace std;

class Person{
  public:
    string name;
    int age;
  
    static void test(string name){
      cout << "Hello " << name << endl;
    }

    //Constructor
    Person(string n, int a){
      name = n;
      age = a;
    }

    //Default Constructor
    Person();

};

int main(){
  Person hatix = Person("Htx", 20);
  /* hatix.name = "Htx"; */
  /* hatix.age = 19; */
  cout << hatix.name << " is " << hatix.age << " years old !" << endl;
  Person::test("bengy"); //we call static method with ::
  /* Person other; */
  return 0;
}
