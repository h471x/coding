#include <iostream>
#include <cmath>
#include "complexe.h"

using namespace std;

Complexe::Complexe() : real_part(0), imaginary_part(0) {}

Complexe::Complexe(float x, float y, char n) : 
  real_part(x), imaginary_part(y), c_name(n){
}

Complexe::~Complexe(){}

//getters
float Complexe::get_real(){return real_part;}
float Complexe::get_imaginary(){return imaginary_part;}

//setters
void Complexe::set_real(float x){real_part = x;}
void Complexe::set_imaginary(float y){imaginary_part = y;}
void Complexe::set_name(char n){c_name = n;}

//display
void Complexe::display(){
  char sign = '+';
  if(imaginary_part < 0) sign = '-';
  cout << this->c_name << " = "<< real_part << " " << sign << " " << abs(imaginary_part) << "i" << endl;
}

Complexe& Complexe::operator+(const Complexe& c){
  real_part += c.real_part;
  imaginary_part += c.imaginary_part;
  return *this;
}
