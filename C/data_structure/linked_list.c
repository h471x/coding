#include <stdio.h>
#include <stdlib.h>

// Define a struct to represent our node
typedef struct{
  void *next;
  int data;
} Node;

Node *head = NULL;

// Add a node to the list
Node *addNode(int data){
  Node *new = NULL; // Declare our node out of his struct
  // We have 2 cases here :
  // First, the list is empty
  if(head == NULL){
    new = malloc(sizeof(Node));
    if(new == NULL) return NULL;
    new->data = data;
    head = new;
    new->next = NULL;
  // The second we have already some item(s) in the list
  }else{
    new = malloc(sizeof(Node));
    if(new == NULL) return NULL;
    new->data = data;
    new->next = head;
    head = new;
  }
  return new;
}

// Remove a node from the list
int removeNode(int data){
  Node *current = head;
  Node *prev = head;
  while(current != NULL){
    if(current->data == data){
      // One case : the current node is the list head
      if(current == head){
        head = current->next;
      }else{
        prev->next = current->next;
        free(current);
        current = NULL;
      }
      return 1; // Yup we find the data to remove
    }
    // Otherwise we didn't find it
    prev = current;
    current = current->next;
  }
  // Otherwise we're in the end of the list
  return 0; // We didn't find the data
}

// Insert a node to the list
Node *insertData(int data, int position){
  Node *current = head;
  while(current != NULL && position != 0){
    position--;
  }
  if(position != 0){
    printf("Position beyond the list element position possible\n");
    return NULL;
  }

  Node *new = malloc(sizeof(Node));
  if(new == NULL) return NULL;

  new->data = data;
  new->next = current->next;
  current->next = new;

  return new;
}

// Print the current list
void showList(){
  Node *current = head;
  while(current != NULL){
    printf("%d->", current->data);
    current = current->next;
  }
  printf("\n");
  return;
}

// Here the menu where the user will interact with the list
void ShowTheMenu(){
  printf("\tOptions : \n\n");
  printf("\t1. Add a node to the list \n");
  printf("\t2. Remove a node from the list \n");
  printf("\t3. Insert a node by position to the list \n");
  printf("\t4. Print the list \n");
  printf("\t5. Exit \n");
  return;
}

int main(int argc, char **argv){
  int option = -1;
  int arg1 = 0;
  int arg2 = 0;
  while(option != 5){
    ShowTheMenu();
    int num_selected = scanf("%d", &option);
    if(num_selected == 1 && option > 0 && option < 5){
      switch(option){
        case 1:
          // Add operation
          printf("Data to insert : ");
          scanf("%d", &arg1);
          Node *new  = addNode(arg1);
          break;
        case 2:
          // Delete operation
          printf("Data to remove : ");
          scanf("%d", &arg1);
          int success = removeNode(arg1);
          if(!success) printf("Sorry We didn't find that data \n");
          break;
        case 3:
          // Insert operation
          printf("Data to insert : ");
          scanf("%d", &arg1);
          printf("Position of insertion : ");
          scanf("%d", &arg2);
          Node *new2 = insertData(arg1, arg2);
          if(new2 == NULL) printf("Sorry failed to insert that data \n");
          break;
        case 4:
          // Print the list
          showList();
          break;
        case 5:
          // Exit the program
          break;
      }
    }
  }
  return 0;
}
