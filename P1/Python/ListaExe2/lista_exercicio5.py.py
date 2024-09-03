lista = []
for i in range(6):
 numero = int(input("digite um numero: "))
 lista.append(numero)
soma = sum(lista)
media = soma/6
print("a soma dos numeros é: ", soma)
print("a media é: " + str(media))
