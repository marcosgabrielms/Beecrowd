def main():

    gremio_v = 0
    inter_v = 0
    empates = 0
    grenais = 0
    escolha = 1

    while escolha != 2:
        x, y = map(int, input().split())
        grenais +=1
        
        if x > y:
            inter_v += 1
        elif y > x:
            gremio_v += 1
        else:
            empates += 1 
        
        print("Novo grenal (1-sim 2-nao)")
        escolha = int(input())
    
    print(f"{grenais} grenais")
    print(f"Inter:{inter_v}")
    print(f"Gremio:{gremio_v}")
    print(f"Empates:{empates}")

    if gremio_v > inter_v:
        print("Gremio venceu mais")
    elif inter_v > gremio_v:
        print("Inter venceu mais")
    else:
        print("Não houve vencedor")            

      
main()