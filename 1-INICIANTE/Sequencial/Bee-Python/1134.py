alcool = 0
gasolina = 0
diesel = 0
c = 0
while c != 4:
    try:
        c = int(input())
        
        if c == 1:
            alcool += 1
        elif c == 2:
            gasolina += 1
        elif c == 3:
            diesel += 1      
    except EOFError:
        break
    except ValueError:
        continue

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")