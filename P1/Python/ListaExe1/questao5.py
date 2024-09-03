gerente = 8500
analista = 5000
suporte = 3000
porcentagem_g = (8500 * 12) / 100
print(porcentagem_g)
porcentagem_a = (5000 * 12) / 100
print(porcentagem_a)
porcentagem_s = (3000 * 15) / 100
print(porcentagem_s)

reajuste_gerente = gerente + porcentagem_g
print("o novo valor do gerente será " + str(reajuste_gerente))
reajuste_analista = analista + porcentagem_a
print("o novo valor do analista será " + str(reajuste_analista))
reajuste_suporte = suporte + porcentagem_s
print("o novo valor do suporte será " + str(reajuste_suporte))
