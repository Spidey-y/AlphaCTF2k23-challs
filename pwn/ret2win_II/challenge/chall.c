#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <seccomp.h>
#define MAX_SIZE 512 
#define MAX_ENTRIES 3
unsigned int created_entries = 0; 
unsigned int freed_entries = 4;
char *entries[MAX_ENTRIES];
void disable_buffering();
void add_entry();
void remove_entry();
void read_entry(); 
void win();
void menu(); 
int get_option();
void sandbox();

int main(int argc, char *argv[]) {
    disable_buffering(); 
    printf("Here is a gift: %p\n", &win);
    printf("Here is another gift: %p\n", &printf);
    int option = 0; 

    while(1) {
        menu(); 
        option = get_option(); 
        switch(option) {
            case 1:
                add_entry();
                break; 
            case 2:
                read_entry(); 
                break;
            case 3:
                remove_entry();
                break; 
            case 4:
                exit(0);
                break; 
            default:
                printf("Invalid option\n");
                break; 

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
    puts("1- Add entry"); 
    puts("2- Read entry"); 
    puts("3- Remove entry"); 
    puts("4- Exit");
}

int get_option() {

    
    int option; 
    int c = 0; 

    printf("Enter an option: ");

    scanf("%d", &option);

    // get rid of new line
    c = getchar();
    return option;

}

void add_entry() {
    fflush(stdin); 
    int c = 0; 
    char size_buffer[7];
    unsigned int size = 0; 
    char *ptr = NULL; 
    int input_length = 0;

    if (created_entries >= MAX_ENTRIES || created_entries < 0) {
        printf("Max entries reached\n");
        exit(0);
    }
    printf("Size: "); 
    fgets(size_buffer, 5, stdin);
    size = atoi(size_buffer);
    if (size <= 0 || size > MAX_SIZE) {
        printf("Invalid size\n"); 
        exit(0);
    }

    ptr = malloc(sizeof(char) * size);
    printf("Content: ");
    input_length = read(0, ptr, size);
    ptr[input_length+1] = '\0'; 
    entries[created_entries] = ptr; 
    created_entries++; 
    printf("Entry added\n");
}

void read_entry() {

    unsigned int index = 0; 
    printf("Entry index: "); 
    scanf("%d", &index);

    if (index < 0 || index > MAX_ENTRIES) {
        printf("Invalid index\n"); 
        exit(0);
    }

    if (entries[index] == 0) {
        printf("Already deleted\n"); 
        exit(0);
    }
    printf("Content: %s\n", entries[index]);
}

void remove_entry() {
    unsigned int index = 0;
    printf("Entry index: "); 
    scanf("%d", &index);

    if (index < 0 || index > MAX_ENTRIES) {
        printf("Invalid index\n"); 
        exit(0);
    }

    if (freed_entries <= 0) {
        printf("Max freed entries reached\n");
        exit(0);
    }

    free(entries[index]); 
    printf("Entry removed\n"); 
    freed_entries--;
    created_entries--;
}

void win() {
    char buffer[40];
    memset(buffer, 0, 40);
    FILE *fd = fopen("./flag.txt", "r");

    if (fd == NULL) {
        printf("Error while opening flag file"); 
        exit(0);
    }

    fgets(buffer, 39, fd);
    write(1, buffer, strlen(buffer));
    fclose(fd);
}

void sandbox() {
    scmp_filter_ctx ctx = seccomp_init(SCMP_ACT_ALLOW);
    if (ctx == NULL) {
        fprintf(stderr, "seccomp error\n");
        exit(EXIT_FAILURE);
    }

    seccomp_rule_add(ctx, SCMP_ACT_KILL, SCMP_SYS(execve), 0);
    
    if (seccomp_load(ctx) < 0) {
        seccomp_release(ctx); 
        exit(EXIT_FAILURE);
    }
    seccomp_release(ctx);
}