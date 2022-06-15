
#atribuição de variáveis
sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

#cálculos
total = sp + rj + mg + es + outros
spcento = sp * 100 / total
rjcento = rj * 100 / total
mgcento = mg * 100 / total
escento = es * 100 / total
outroscento = outros * 100 / total

#mostrando os resultados
print("-="*50)
print(f"Faturamento total: R${total:.2f}")
print('Representação de cada estado em percentual:')
print(f'SP - {spcento:.2f}%')
print(f'RJ - {rjcento:.2f}%')
print(f'MG - {mgcento:.2f}%')
print(f'ES - {escento:.2f}%')
print(f'Outros - {outroscento:.2f}%')
print("-="*50)
