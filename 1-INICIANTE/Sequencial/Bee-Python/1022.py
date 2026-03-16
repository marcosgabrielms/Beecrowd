def mdc(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def main():
    n = int(input())

    for _ in range(n):
        entrada = input().split()

        numerador1 = int(entrada[0])
        denominador1 = int(entrada[2])
        operador = entrada[3]
        numerador2 = int(entrada[4])
        denominador2 = int(entrada[6])

        if operador == '+':
            num = numerador1 * denominador2 + numerador2 * denominador1
            den = denominador1 * denominador2
        elif operador == '-':
            num = numerador1 * denominador2 - numerador2 * denominador1
            den = denominador1 * denominador2
        elif operador == '*':
            num = numerador1 * numerador2
            den = denominador1 * denominador2
        elif operador == '/':
            num = numerador1 * denominador2
            den = numerador2 * denominador1

        
        divisor = mdc(num, den)
        num_simples = num // divisor
        den_simples = den // divisor

        print(f"{num}/{den} = {num_simples}/{den_simples}")

if __name__ == '__main__':
    main()
