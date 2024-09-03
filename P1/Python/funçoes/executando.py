import funçoes
nome = input("Digite seu nome: ")
idade = int(input("Digite o ano que você nasceu: "))
print("seu nome possui {} letras".format(funçoes.tamanho(nome)))
print("você tem {} anos".format(funçoes.idade(idade)))