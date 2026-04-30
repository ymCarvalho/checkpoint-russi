# Maria Beatriz Braga de Lima

'''
PROGRAMA DE IMPOSTOS SOBRE CARGAS
DE CAMINHÕES
'''

#===========
# VARIAVEIS
#===========
estado = int(input("Digite o código do estado de origem da carga (de 1 a 5): "))
peso_carga = float(input("Digite o peso da carga (em toneladas): "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

#=================================
# CONVERSÃO DE TONELADAS PARA KG
#=================================
peso_kg = peso_carga * 1000
print(f"O peso da carga é {peso_kg} Kg.")

#================
# PREÇO DA CARGA
#================
if codigo_carga >= 10 and codigo_carga <= 20:
    preco_carga = peso_kg * 100
    print(f"O preço da carga é R$ {preco_carga:.2f} reais. ")
elif codigo_carga >= 21 and codigo_carga <= 30:
    preco_carga = peso_kg * 250
    print(f"O preço da carga é R$ {preco_carga:.2f} reais. ")
elif codigo_carga >= 31 and codigo_carga <= 40:
    preco_carga = peso_kg * 340
    print(f"O preço da carga é R$ {preco_carga:.2f} reais. ")

#==========
# IMPOSTOS
#==========
if estado == 1:
    imposto = preco_carga * 0.35
    print(f"O valor do imposto será de R$ {imposto:.2f} reais.")
elif estado == 2:
    imposto = preco_carga * 0.25
    print(f"O valor do imposto será de R$ {imposto:.2f} reais.")
elif estado == 3:
    imposto = preco_carga * 0.15
    print(f"O valor do imposto será de R$ {imposto:.2f} reais.")
elif estado == 4:
    imposto = preco_carga * 0.05
    print(f"O valor do imposto será de R$ {imposto:.2f} reais.")
else:
    imposto = 0
    print(f"O valor do imposto será de R$ {imposto:.2f} reais.")

#=============
# VALOR TOTAL
#=============
valor_total = preco_carga + imposto
print(f"O valor total sobre a carga é de R$ {valor_total:.2f} reais.")








