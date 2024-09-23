#include <stdio.h>

void decorate_name(const char* name) {
    printf("<<< %s >>>\n", name);
}

int main() {
    char name[100];
     printf("Please enter your name: ");
    fgets(name, sizeof(name), stdin);
    size_t len = strlen(name);
    if (len > 0 && name[len - 1] == '\n') {
        name[len - 1] = '\0';
    return 0;}
}