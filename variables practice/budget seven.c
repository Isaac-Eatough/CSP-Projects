#include <stdio.h>

int main(void){
    float income, rent, utilities, groceries, transportation, expenses, savings, total;
    float prent, putilities, pgroceries, ptransportation, pexpenses;
    printf("This is going to calculte you budget for the month\n");
    printf("How much do you make a month?\n");
    scanf("%f", &income);
    printf("How much do you make a rent?\n");
    scanf("%f", &rent);
    printf("How much do you make a utilities?\n");
    scanf("%f", &utilities);
    printf("How much do you make a groceries?\n");
    scanf("%f", &groceries);
    printf("How much do you make a transportation?\n");
    scanf("%f", &transportation);
    expenses = rent + utilities + groceries + transportation;
    savings = income *.2;
    total = income + expenses + expenses;
    prent = rent/income;
    putilities = utilities/income;
    pgroceries = groceries/income;
    ptransportation = transportation/income;
    pexpenses = expenses/income;
    printf("your income is: $%.2f\n", income);
    printf("your expenses is: $%.2f\n", expenses);
    printf("your savings is: $%.2f\n", total);
    printf("your rent is %.2f", prent);

    return 0;
}