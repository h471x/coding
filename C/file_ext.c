#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
  if (argc != 2) {
    printf("Usage: %s <nom_fichier>\n", argv[0]);
    return 1;
  }

  char *nomFichier = argv[1];
  char *extension = strrchr(nomFichier, '.');

  if (extension == NULL || strcmp(extension, ".htx") != 0) {
    printf("Erreur d'extension de fichier. Veuillez utiliser un fichier avec l'extension .htx.\n");
    return 1;
  }

  FILE *fichier = fopen(nomFichier, "a+");

  if (fichier == NULL) {
    printf("Erreur lors de l'ouverture du fichier.\n");
    return 1;
  }

  char donnees[100];

  printf("Saisis tes donnees (max 100 caracteres) : ");
  fgets(donnees, sizeof(donnees), stdin);

  if (ftell(fichier) == 0) {
    fprintf(fichier, "%s", donnees);
    printf("Donnees ecrites dans le fichier %s avec succes !\n", nomFichier);
  } else {
    fprintf(fichier, "\n%s", donnees);
    printf("Donnees ajoutees au fichier %s avec succes !\n", nomFichier);
  }

  fclose(fichier);

  return 0;
}
