import math
a = int(input("valor de a"))
b = int(input("valor de b"))
c = int(input("valor de c"))
delta = (b ** 2) - 4 * a * c
print(delta)
if delta < 0 :
  print("essa equação não possui raízes reais")
elif delta == 0 :
 x1 = (-b + math.sqrt,delta) / (2 * a)
 print(x1)
elif delta > 0 :
 x1 = (-b + math.sqrt,delta) / (2 * a)
 x2 = (-b -math.sqrt,delta) / (2 * a)
 print(x1)
 print(x2)


