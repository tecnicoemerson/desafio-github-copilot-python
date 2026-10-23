num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))  

operacao = input("Digite a operação desejada (+, -, *, /): ") 

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = abs(num1 - num2)
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
        resultado = None
else:
    print("Erro: Operação inválida.")
    resultado = None

if resultado is not None:
    print("Resultado da operação:", resultado)