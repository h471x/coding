#ifndef COMPLEXE_H
#define COMPLEXE_H

class Complexe{
  private:
    float real_part;
    float imaginary_part;
    char c_name;

  public:
    Complexe(); //Default constructor
    Complexe(float x, float y, char name); //Another constructor
    ~Complexe(); //Destructor

    //method
    Complexe& operator+(const Complexe& c);

    //Getters
    float get_real();
    float get_imaginary();

    //Setters
    void set_real(float x);
    void set_imaginary(float y);
    void set_name(char n);

    //display method
    void display();
};

#endif // COMPLEXE_H
#define COMPLEXE_H
