# Receber o valor que o funcionário ganha por hora em reais
# e número de horas trabalhadas no mês em inteiro
# Exibir:
# a) O valor total do salário no mês (bruto)
# b) O valor a ser pago ao INSS
# c) O valor da taxa sindical
# d) Salário líquido após itens b e c
#
# INSS     8%
# Sindical 5%

while True:
    try:
        salario = float(input("Digite o salário: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números reais.")


while True:
    try:
        horas = int(input("Digite o número de horas: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")
 

salario_bruto = salario * horas
inss = salario_bruto * 0.08
sindical = salario_bruto * 0.05
salario_liquido = salario_bruto - ( inss + sindical )


print(salario_bruto)
print(inss)
print(sindical)
print(salario_liquido)