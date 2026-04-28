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
#lado maior, menor e meio
#===================================
if ladoA >= ladoB and ladoA >= ladoC:
    maior = ladoA
    if ladoB >= ladoC:
        medio = ladoB
        menor = ladoC
    else:
        medio = ladoC
        menor = ladoB

elif ladoB >= ladoA and ladoB >= ladoC:
    maior = ladoB
    if ladoA >= ladoC:
        medio = ladoA
        menor = ladoC
    else:
        medio = ladoC
        menor = ladoA

else:
    maior = ladoC
    if ladoA >= ladoB:
        medio = ladoA
        menor = ladoB
    else:
        medio = ladoB
        menor = ladoA

#=====================
# casos dos triângulos
#=====================
if maior >= (medio + menor):
    print(f"NÃO FORMA TRIÂNGULO!")
else:
    if maior == medio and maior == menor:
        print(f"TRIÂNGULO EQUILÁTERO")
    elif maior == medio != menor or maior == menor != medio or menor == medio != maior:
        print(f"TRIÂNGULO ISÓSCELES")
    else:
        if maior**2 == medio**2 + menor**2:
            print(f"TRIÂNGULO RETÂNGULO")
        elif maior**2 > medio**2 + menor**2:
            print(f"TRIÂNGULO OBTUSÂNGULO")
        else:
            print(f"TRIÂNGULO ACUTÂNGULO")