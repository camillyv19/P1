#Crie uma lista que receba valores inteiro do usuário até que o usuário queira para de inserir
#valores (colocar uma condição de parada), faça a soma e retorne o resultado para o usuário.
lista = []
while True:
  valor = input("Digite um número a ser somado \nou digite fim para sair: ")
  if valor == "fim":
    break
  lista.append(int(valor))
soma = sum(lista)
print(soma)