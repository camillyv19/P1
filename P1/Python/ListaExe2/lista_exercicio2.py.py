valor = int(input("digite um valor "))
for i in range(valor+1):
  if valor % 2 == 0:
    if i % 2 == 0:
      print(i)
  else:
    if i % 2 != 0:
      print(i)

