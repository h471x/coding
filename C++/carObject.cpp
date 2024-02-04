#include <iostream>
using namespace std;

// Creating a class called Car
class Car {
  private:
    string brand;
    string model;
    int year;

  public:
    // Constructor - called when creating an object of the class
    Car(string b, string m, int y) {
        brand = b;
        model = m;
        year = y;
    }

    // Method to display the car details
    void displayDetails() {
        cout << "Brand: " << brand << endl;
        cout << "Model: " << model << endl;
        cout << "Year: " << year << endl;
    }
};

int main() {
    // Creating an object of the class Car
    Car myCar("Toyota", "Camry", 2022);

    // Calling the displayDetails method on the object
    myCar.displayDetails();

    return 0;
}
