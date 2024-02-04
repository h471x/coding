#include <iostream>
#include "complexe.h"

int main(int argc, char *argv[]){
  Complexe c1(5,-3, 'a'), c2(-1,3, 'b'), c3(1,2, 'c');
  Complexe resultat; 
  c1.display();
  c2.display();
  c3.display();
  c1.operator +(c2);
  resultat = c1 + c3;
  resultat.set_name('x');
  resultat.display();
  return 0;
}
