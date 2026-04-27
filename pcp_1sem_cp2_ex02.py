# João Pedro Santos Ferreira
# Maria Beatriz Braga de Lima

'''
PROGRAMA DE ANÁLISE
DE CASOS
DE TRIÂNGULOS
'''

#=========================================================
# interação com o usuário (tamanho dos lados do triângulo)
#=========================================================
ladoA = float(input("Digite o tamanho do lado A do triângulo: "))
ladoB = float(input("Digite o tamanho do lado B do triângulo: "))
ladoC = float(input("Digite o tamanho do lado C do triângulo: "))

#===================================
#ordem decrescente - if (lado maior)
#===================================
if ladoA >= ladoB and ladoA >= ladoC:
    maior = ladoA
elif ladoB >= ladoA and ladoB >= ladoC:
    maior = ladoB
else:
    maior = ladoC

#================
# if (lado medio)
#================
if ladoA < ladoB and ladoA >= ladoC:
    medio = ladoA
elif ladoB > ladoA and ladoB <= ladoC:
    medio = ladoB
else:
    medio = ladoC

#===============
#if (lado menor)
#===============
if ladoA <= ladoB and ladoA <= ladoC:
    menor = ladoA
elif ladoB < ladoA and ladoB <= ladoC:
    menor = ladoB
else:
    menor = ladoC

#=====================
# casos dos triângulos
#=====================
if maior >= (medio + menor):
    print(f"NÃO FORMA TRIÂNGULO!")
else:
    if maior**2 == medio**2 + menor**2:
        print(f"TRIÂNGULO RETÂNGULO")
    elif maior**2 > medio**2 + menor**2:
        print(f"TRIÂNGULO OBTUSÂNGULO")
    else:
        print(f"TRIÂNGULO ACUTÂNGULO")

    if maior == medio and maior == menor:
        print(f"TRIÂNGULO EQUILÁTERO")
    elif maior == medio != menor or maior == menor != medio or menor == medio != maior:
        print(f"TRIÂNGULO ISÓSCELES")