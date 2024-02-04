#include <stdio.h>
#include <stdlib.h>

#define size 100

FILE *file; // global declaration of file
char *data; // global declaration of data

void init(void) {
  data = (char*)malloc(size); // Allocation de mémoire pour la variable data
}

void openFile(void) {
  file = fopen("data.htx", "w"); // Ouverture en mode écriture
  if (file == NULL) {
    printf("Erreur d'ouverture du fichier !");
    exit(1); // Quitte le programme avec un code d'erreur
  }
}

void writeFile(void) {
  printf("Saisis les données : ");
  fgets(data, 100, stdin);

  if (ftell(file) == 0) {
    fprintf(file, "%s", data);
    printf("Donnees ecrites dans le fichier !\n");
  }else{
    fprintf(file, "\n%s", data);
    printf("Donnees ajoutees au fichier !\n");
  }

  fclose(file);
}
