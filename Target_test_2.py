# importando json e abrindo o arquivo.
import json

with open('dados.json') as jsonfile:
    dados = json.load(jsonfile)

# atribuindo as variáveis necessárias
menor = maior = soma = cont = media_acima = 0

# sistema de repetição para o cálculo de maior, menor, soma.
for dia in dados:
    if dia['valor'] > 0:
        if cont == 0:
            menor = maior = soma = dia['valor']
            cont = cont + 1
        else:
            soma = soma + dia['valor']
            if dia['valor'] > maior:
                maior = dia['valor']
            elif dia['valor'] < menor:
                menor = dia['valor']
            cont = cont + 1

# cálculo da média
media = soma / cont
# cálculo de dias acima da média

for dia in dados:
    if dia['valor'] > media:
        media_acima += 1

# mostrando todos os resultados
print('*'*50)
print(f'O maior valor faturado em um dia foi R${maior:.2f}.')
print(f'O menor valor faturado em um dia foi R${menor:.2f}.')
print(
    f'A média mensal é R${media:.2f} e em {media_acima} dias o faturamento foi acima da média.')
print(f'A soma total de todos os dias é de: R${soma:.2f}.')
print('*'*50)
