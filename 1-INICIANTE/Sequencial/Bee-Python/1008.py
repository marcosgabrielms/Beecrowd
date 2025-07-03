def main():

    numero_func = int(input())
    num_hora_trabalhada = int(input())
    valor_por_hora = float(input())

    salario = num_hora_trabalhada * valor_por_hora

    print(f"NUMBER = {numero_func}")
    print(f"SALARY = U$ {salario:.2f}")

if __name__ == '__main__':
    main()

