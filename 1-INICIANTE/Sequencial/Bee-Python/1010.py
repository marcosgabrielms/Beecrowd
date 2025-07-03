def main():

    cod_peca1, qtd_peca1, valor_peca1 = map(float, input().split())
    cod_peca2, qtd_peca2, valor_peca2 = map(float, input().split())

    total_peca1 = qtd_peca1 * valor_peca1
    total_peca2 = qtd_peca2 * valor_peca2

    total_a_pagar = total_peca1 + total_peca2

    print(f"VALOR A PAGAR: R$ {total_a_pagar:.2f}")

if __name__ == '__main__':
    main()
