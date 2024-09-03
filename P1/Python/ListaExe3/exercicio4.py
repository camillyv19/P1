def decimalLetra(letra):
  alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y","Z"]
  elemento = letra.upper()
  indice = alfabeto.index(elemento) + 1
  print("O elemento {} corresponde ao decimal {}".format(elemento,indice))

def impaPar(indice):
  if indice % 2 == 0:
    for i in range(2, indice, 2):
      print(i)
  else:
    for i in range(1, indice, 2):
      print(i)
