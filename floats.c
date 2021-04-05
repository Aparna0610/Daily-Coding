#include <stdio.h>
#include <cs50.h>

int main(void)
{
    float x = get_float("Enter x: \n");
    float y = get_float("Enter y: \n");

    printf("x/y = %.2f\n", x/y);
}
