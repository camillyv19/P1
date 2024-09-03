from datetime import datetime
idade = int(input("qual é a sua idade? "))
ano = datetime.now().year
ano_nascimento = idade - ano
print("voce nasceu em" + str(ano_nascimento))