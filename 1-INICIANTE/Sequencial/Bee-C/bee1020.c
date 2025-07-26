#include <stdio.h>

int main() {

    int total_dias;

    int anos, meses, dias;

    scanf("%d", &total_dias);

    anos = total_dias / 365;

    meses = (total_dias % 365) / 30;

    dias = (total_dias % 365) % 30;

    printf("%d ano(s)\n", anos);
    printf("%d mes(es)\n", meses);
    printf("%d dia(s)\n", dias);

    return 0;
}