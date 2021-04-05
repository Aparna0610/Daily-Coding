#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int age = get_int("Enter your age:\n");
    //int age_in_days = age * 365;
    printf("Your age in days: %i\n", age * 365);
}
