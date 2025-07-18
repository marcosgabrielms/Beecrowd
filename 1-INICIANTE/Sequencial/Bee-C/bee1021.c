#include <stdio.h>

int main() {
    
    double valor;
    int total_centavos;

    scanf("%lf", &valor);
    total_centavos = (int)(valor * 100 + 0.5);

    printf("NOTAS:\n");

    int notas[] = {10000, 5000, 2000, 1000, 500, 200};

    for (int i = 0; i < 6; i++) {
        int quantidade = total_centavos / notas[i];
        printf("%d nota(s) de R$ %.2f\n", quantidade, notas[i] / 100.0);
        total_centavos %= notas[i];
    }

    printf("MOEDAS:\n");

    int moedas[] = {100, 50, 25, 10, 5, 1};
    for (int i = 0; i < 6; i++) {
        int quantidade = total_centavos / moedas[i];
        printf("%d moeda(s) de R$ %.2f\n", quantidade, moedas[i] / 100.0);
        total_centavos %= moedas[i];
    }
    return 0;
}