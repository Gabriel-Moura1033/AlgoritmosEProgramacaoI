num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
 
print(f"Soma: {num1 + num2}")
print(f"Subtração: {num1 - num2}")
print(f"Multiplicação: {num1 * num2}")
 
if num2 != 0:
    print(f"Divisão: {num1 / num2}")
    print(f"Divisão truncada: {num1 // num2}")
    print(f"Resto: {num1 % num2}")
else:
    print("Divisão: Impossível dividir por zero") 

print(f"Exponenciação: {num1 ** num2}")