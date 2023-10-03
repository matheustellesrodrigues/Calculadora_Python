num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

class Calcular():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Somar(self):
        return self.num1 + self.num2
    
    def Dividir(self):
        return self.num1 / self.num2
    
    def Multiplicar(self):
        return self.num1 * self.num2
    
    def Subtracao(self):
        return self.num1 - self.num2

soma = Calcular(num1, num2)
while True:
    print("1 - Realizar Soma: ")
    print("2 - Realizar Divisão: ")
    print("3 - Realizar Multiplicação: ")
    print("4 - Realizar Subtração: ")
    print("5 - Sair: ")
    print("6 - Realizar conta com numeros diferentes: ")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"O resultado da Soma deu: {soma.Somar()}")
        
    elif opcao == 2:
        print(f"O resultado da Divisão deu: {soma.Dividir()}")

    elif opcao == 3:
        print(f"O resultado da Multiplicação deu: {soma.Multiplicar()}")

    elif opcao == 4:
        print(f"O resultado da Subtração deu: {soma.Subtracao()}")

    elif opcao == 5:
        print("Obrigado por usar a nossa calculadora.")
        break

    elif opcao == 6:
        num1 = int(input("Digite o primeiro numero: "))
        num2 = int(input("Digite o segundo numero: "))
        soma = Calcular(num1, num2)

    else:
        print("Número inválido")
    


    