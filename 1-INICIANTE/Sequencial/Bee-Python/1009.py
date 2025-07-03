def main():

    vendedor = str(input())
    salario_fixo = float(input())
    vendas_efetuadas = float(input())

    comissao = 0.15 * vendas_efetuadas

    total_a_receber = salario_fixo + comissao

    print(f"TOTAL = R$ {total_a_receber:.2f}")
    
if __name__ == '__main__':
    main()