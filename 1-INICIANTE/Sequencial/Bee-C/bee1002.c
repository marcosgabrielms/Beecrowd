#include <stdio.h>
#include <math.h>

int main() {

    double raio;
    double area_circulo;
    double pi = 3.14159;
    
    scanf("%lf", &raio);

   area_circulo = pi * (raio * raio);

   printf("A=%.4f\n", area_circulo);

   return 0;
}