area = int(input("Digite a �rea a aser pintada: "))


litros = area//3
if area % 3 > 0:
    litros = litros + 1
    
latas = litros//18
if litros % 18 > 0:
    latas = latas + 1

print("Voce precisara de", latas, "latas.")
print("Voce vai pagar R$", latas*80)
