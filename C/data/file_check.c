#include <stdio.h>
#include <stdlib.h>

#define size 100

FILE *file; // Déclaration globale du fichier
char *data; // Déclaration globale de la variable data

void init(void);
void openFile(void);
void writeFile(void);

int main(int argc, char *argv[]) {
  init();
  openFile();
  writeFile();
  return 0;
}

void init(void) {
  data = (char*)malloc(size); // Allocation de mémoire pour la variable data
}

void openFile(void) {
  file = fopen("data.htx", "a+"); // Ouverture en mode écriture
  if (file == NULL) {
    printf("Erreur d'ouverture du fichier !");
    exit(1); // Quitte le programme avec un code d'erreur
  }
}

void writeFile(void) {
  printf("Saisis les données : ");
  fgets(data, 100, stdin);

  if (ftell(file) == 0) {
    fprintf(file, "\t%s", data);
    printf("Donnees ecrites dans le fichier !\n");
  }else{
    fprintf(file, "\t%s", data);
    printf("Donnees ajoutees au fichier !\n");
  }

  fclose(file);
}
