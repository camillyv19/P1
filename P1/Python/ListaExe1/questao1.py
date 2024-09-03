num1 = int(input("digite o primeiro valor: "))
num2 = int(input("digite o segundo valor: "))
print('''[1] somar
[2] subtrair
[3] multiplicar
[4] dividir''')
opcao = int(input("qual a sua opção?"))
if opcao == 1:
 somar = num1 + num2
 print("seu resultado é" , somar)
elif opcao == 2:
 subtrair = num1 - num2
 print("seu resultado é" , subtrair)
elif opcao == 3:
 multiplicar = num1 * num2
 print("seu resultando é" , multiplicar)
elif opcao == 4:
 dividir = num1 / num2
 print("seu resultado é" , dividir)
