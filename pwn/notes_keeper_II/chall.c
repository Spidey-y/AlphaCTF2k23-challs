#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <assert.h>

#define MAX_SIZE 1110
#define MAX_ENTRIES 20
void disable_buffering(); 
void menu();
int get_option();
void add_note();
void remove_note();
void edit_note();
void view_note();
void gadget();
char *entries[MAX_ENTRIES]; 
char created_entries = 0;

int main(int argc, char *argv[]) {
    disable_buffering(); 

    while(1) {
        
        menu(); 
        switch(get_option()) {
            case 1:
                add_note();
                break; 
            case 2: 
                remove_note();
                break; 

            case 3:
                edit_note();
                break;
            case 4:
                view_note();
                break; 
            case 5 : 
                printf("Good bye\n");
                return 0;
            default:
                printf("Invalid option\n");
        }
    }

    return 0;
}

void disable_buffering() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void menu() {
    puts("1- Add note");
    puts("2- Remove note");
    puts("3- Edit note");
    puts("4- View note");
    puts("5- Exit");

}

int get_option() {

    int option; 
    int c = 0; 

    printf("Enter an option: ");
    scanf("%d", &option);
    c = getchar();
    return option;
}

void add_note() {

    int c = 0; 
    char size_buffer[10];
    unsigned int size = 0; 
    char *ptr = NULL; 
    int input_length = 0;

    if (created_entries >= MAX_ENTRIES) {
        printf("Maximum notes reached\n");
        return;
    }

    printf("Size: "); 
    fgets(size_buffer, 8, stdin);

    size = atoi(size_buffer); 
    if (size <= 0 || size > MAX_SIZE) {
        printf("Invalid size\n");
        return;
    }

    ptr = malloc(sizeof(char) * size);
    if (ptr == NULL) {
        printf("Error occured while allocating memory");
        return;
    }

    printf("Note content: ");
    input_length = read(0, ptr, size - 1);
    entries[created_entries] = ptr; 

    created_entries++; 
    printf("Note added\n");

}

void remove_note() {

    unsigned int index = 0;
    printf("Note index: "); 
    scanf("%d", &index); 

    if (index < 0 ) {
        printf("Invalid index\n");
        return;
    }

    free(entries[index]);
    entries[index] = 0;
    created_entries--; 

    printf("Note removed\n");
}

void view_note() {
    int index = 0; 

    printf("Index: ");
    scanf("%d", &index);

    if (index > MAX_ENTRIES) {
        printf("Invalid index\n");
        return;
    }
    if (entries[index] == 0) {
        printf("This note has been deleted already\n");
        return;
    }

    printf("%s\n", entries[index]);

}


void edit_note() {

    int index = 0 ;
    printf("Index: "); 
    scanf("%d", &index); 

    if (index < 0 || index > MAX_ENTRIES) {
        printf("Invalid index\n"); 
        return;
    }

    if (entries[index] == 0) {
        printf("Note already deleted\n"); 
        return;
    }

    printf("Content: "); 
    read(STDIN_FILENO, entries[index], strlen(entries[index]));
    printf("Note updated\n");
    fflush(stdin);
    char ch = getchar();
    return;
}

void gadget() {

    asm("syscall;ret");
}

