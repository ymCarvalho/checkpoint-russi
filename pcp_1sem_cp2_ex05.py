# =========================
# definindo as funções de cálculo
# =========================
def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= renda * 20:
        return True
    return False


def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05 # 5% de juros ao mes
    elif parcelas <= 12:
        return 0.08 # 8% de juros ao mes
    else:
        return 0.10 # 10% de juros ao mes


def calcular_parcela(valor, taxa, parcelas):
    i = taxa
    n = parcelas
    pmt = valor * (i * (1 + i)**n) / ((1 + i)**n - 1)
    return pmt


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor):
    return total - valor


# =========================
# código principal
# =========================

nome = input("Nome do cliente: ")
idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))
valor = float(input("Valor desejado do empréstimo: "))
parcelas = int(input("Número de parcelas (3 a 24): "))

print("\n--- RESULTADO ---")

if not pode_aprovar(idade, renda, valor):
    print("EMPRÉSTIMO NEGADO")
else:
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    print("EMPRÉSTIMO APROVADO")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: R$ {valor:.2f}")
    print(f"Taxa de juros aplicada: {taxa*100:.1f}% ao mês") # transforma o valor da % em número inteiro
    print(f"Valor da parcela: R$ {parcela:.2f}")
    print(f"Total pago: R$ {total:.2f}")
    print(f"Total de juros: R$ {juros:.2f}")