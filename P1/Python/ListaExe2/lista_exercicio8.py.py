menores25 = 0
maior25menor60 = 0
maior60 = 0
receberIdades = "s"
while receberIdades == "s":
  idade = int(input("Digite a idade: "))
  if idade < 25:
    menores25 = menores25 + 1
  elif idade > 25 and idade <= 60:
    maior25menor60 = maior25menor60 + 1
  else:
    maior60 = maior60 + 1

  receberIdades = input("Deseja receber idades? (s/n)")

print("0 à 25", menores25, "pessoas")
print("26 à 60", maior25menor60, "pessoas")
print("maiores que 60", maior60, "pessoas")