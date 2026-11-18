nome = input("Digite seu nome: ")
idade = input(f"Qual sua idade {nome}? ")
num1 = float(input(f"{nome} digite sua altura: "))
num2 = float(input("Agora digite seu peso: "))
IMC = num2 / (num1*num1)
print(f"{nome} o seu IMC é {IMC:.2f}")
if IMC < 18.5:
    print ("Classificação: Abaixo do peso")
elif IMC < 25:
    print("Classificação: Peso normal")
elif IMC < 30:
    print ("Classificação: Sobrepeso")
elif IMC < 35:
    print ("Classificação: Obesidade grau I")
elif IMC < 40:
    print ("Classificação: Obesidade grau II")
else:
    print("Classificação: Obesidade grau III (mórbida)")