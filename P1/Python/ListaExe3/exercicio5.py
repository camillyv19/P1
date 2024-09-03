def dados(nome, idade, peso, altura, sexo):
    caracteres = len(nome)
    print("Seu nome possui {} caracteres.".format(caracteres))
    idade_usuario = idade
    if idade > 18:
      print("Você é maior de idade!")
    else:
      print("Você é menor de idade!")
    IMC = peso / (altura ** 2)
    print(f"Seu IMC é de {IMC:.2f}")
    if IMC < 18.5:
      print("Você está abaixo do peso ideal.")
    elif IMC >= 18.5 and IMC <= 25:
      print("Você está no peso ideal!")
    else:
      print("Você está acima do peso ideal.")
    sexo_usuario = sexo
    if sexo == "f":
        print("Do sexo femino.")
    else:
        print("Do sexo masculino.")


dados("camilly", 19,68.5, 1.63, "f")
