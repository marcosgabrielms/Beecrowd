def main():

    total_dias = int(input())

    ano = total_dias // 365

    dias_restantes = total_dias %  365

    meses = dias_restantes // 30

    dias = dias_restantes% 30

    print(f"{ano} ano(s)")
    print(f"{meses} mes(es)")
    print(f"{dias} dia(s)")

if __name__ == '__main__':
    main()