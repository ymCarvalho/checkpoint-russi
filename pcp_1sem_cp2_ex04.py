def calcular_horas_extras(salario_base, total_horas):
    hora_extra = (0.015 * salario_base) * total_horas
    return hora_extra


def calcular_descontos_faltas(salario_base, faltas):
    descontos_faltas = (0.02 * salario_base) * faltas
    return descontos_faltas


def calcular_bonus(cargo, bonus):
    if bonus == 's':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0


nome = input("Digite seu nome: ")
cargo = int(input("Digite seu cargo: (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Digite seu salário base: "))
total_horas = int(input("Digite seu total de horas extras: "))
total_faltas = int(input("Digite seu total de faltas: "))
bonus = input("Recebeu bônus? (S ou N): ")


horas_extras = calcular_horas_extras(salario_base, total_horas)
descontos = calcular_descontos_faltas(salario_base, total_faltas)
bonus_valor = calcular_bonus(cargo, bonus)

total_acrescimos = horas_extras + bonus_valor
salario_bruto = salario_base + horas_extras
salario_final = salario_bruto + bonus_valor - descontos

print("\n--- RESUMO ---")
print(f"Salário base: R$ {salario_base:.2f}")
print(f"Horas extras: R$ {horas_extras:.2f}")
print(f"Bônus: R$ {bonus_valor:.2f}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Acréscimos: R$ {total_acrescimos:.2f}")
print(f"Descontos (faltas): R$ {descontos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")