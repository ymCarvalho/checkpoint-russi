# JOÃO PEDRO SANTOS FERREIRA
'''
SISTEMA DE NOTAS
ANALISE SEMESTRAL
'''

#===================
# variáveis - notas
#===================
notacp1 = float(input("Digite a nota do Checkpoint 01: "))
notacp2 = float(input("Digite a nota do Checkpoint 02: "))
notacp3 = float(input("Digite a nota do Checkpoint 03: "))
notasp1 = float(input("Digite a nota do Sprint 01: "))
notasp2 = float(input("Digite a nota do Sprint 02: "))
notags = float(input("Digite a nota da Global Solution: "))

#==============================
# informação para o usuário...
#==============================
if notacp1 <= notacp2 and notacp1 <= notacp3:
    print(f"A nota da CP01: {notacp1} será descartada.")
    menor_cp = notacp1

elif notacp2 <= notacp1 and notacp2 <= notacp3:
    print(f"A nota da CP02: {notacp2} será descartada.")
    menor_cp = notacp2

else:
    print(f"A nota da CP03: {notacp3} será descartada.")
    menor_cp = notacp3

notacp = notacp1 + notacp2 + notacp3 - menor_cp

#================================
# cálculo da média (sem os pesos)
#=================================
media = ((notacp + notasp1 + notasp2) / 4) * 0.4 + notags * 0.6

print(f"A média sem o peso semestral: {media:.1f}")

#================================
# cálculo da média (com os pesos)
#=================================

media_peso = media * 0.4
print(f"A média normal com o peso semestral: {media_peso:.1f}")