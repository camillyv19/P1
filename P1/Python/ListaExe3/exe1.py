def calcular_produto(produto):
    real = produto * 5.09
    return "{:.2f}".format(real)

def calcular_frete(peso):
    if peso > 100:
        frete = (peso / 100) * 1.99
        real = frete * 5.09
        return "{:.2f}".format(real)
    else:
        real = 1.99 * 5.09
        return "{:.2f}".format(real)

