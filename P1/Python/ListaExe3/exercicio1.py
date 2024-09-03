from exe1 import calcular_frete, calcular_produto

produto = str(input("Qual o seu produto? "))
peso = float(input("Qual o peso do produto? "))
valor = float(input("Qual o valor do produto em dólar $"))

peso_real = calcular_frete(peso)
valor_real = calcular_produto(valor)
total = float(peso_real) + float(valor_real)

print("O valor do protuto em real é de R$", peso_real)
print("O frete do produto será R$", valor_real)
print("O total da compra a ser pago é de R$", total)
