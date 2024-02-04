#include <stdio.h>

int main() {
  FILE *fichier;//declaration de fichier en etant pointeur
  char donnees[100];

  fichier = fopen("donnees.htx", "w");//ouvrir le fichier

  if (fichier == NULL) {
    printf("Erreur lors de l'ouverture du fichier.\n");
    return 1;
  }

  printf("Saisis tes donnees (max 100 caracteres) : ");
  fgets(donnees, sizeof(donnees), stdin);

  fprintf(fichier, "%s", donnees);
  printf("Donnees ecrites dans le fichier donnees.txt avec succes !\n");
  fclose(fichier);

  return 0;
}
