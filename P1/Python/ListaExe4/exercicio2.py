feminino = []
masculino = []
cont = "S"
while cont == "S":
    pessoa = dict()
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['idade'] = int(input('Digite a idade: '))
    pessoa['sexo'] = input('Digite o sexo [F/M]: ').upper()
    print("-=" * 30)
    if pessoa['sexo'] == 'F':
        feminino.append(pessoa)
    elif pessoa['sexo'] == 'M':
        masculino.append(pessoa)

    if len(feminino) + len(masculino) >= 10:
       cont = input('Deseja continuar? [S/N]: ').upper()

print("Pessoas do sexo feminino:")
print(feminino)
print("Pessoas do sexo masculino:")
print(masculino)
