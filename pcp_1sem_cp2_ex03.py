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
elif notacp2 <= notacp1 and notacp2 <= notacp3:
    print(f"A nota da CP02: {notacp2} será descartada.")
else:
    print(f"A nota da CP03: {notacp3} será descartada.")

#=============================
# cálculo para os checkpoints
#=============================
if notacp1 <= notacp2 and notacp1 <= notacp3:
    notacp = (notacp2 + notacp3)
elif notacp2 <= notacp1 and notacp2 <= notacp3:
    notacp = (notacp1 + notacp3)
else:
    notacp = (notacp1 + notacp2)

#================================
# cálculo da média (sem os pesos)
#=================================
media = float(((notacp + notasp1 + notasp2) / 4) * 0.4) + notags * 0.6
print(f"A média sem o peso semestral: {media:.1f}")

#================================
# cálculo da média (com os pesos)
#=================================
media_peso = float(media * 0.4)
print(f"A média normal com o peso semestral: {media_peso:.1f}")