#include <stdio.h>
#include <cs50.h>
int main(void)
{
    string answer = get_string("Enter your name:\n");
    printf("Hello, %s\n", answer);
}
