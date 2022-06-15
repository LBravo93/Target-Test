
print("-"*53)
# Variável de números na sequência inserida pelo usuário.
num = int(input("Quantos termos deseja ver na sequência de Fibonacci? "))
print("-"*53)

primeiro = 0
segundo = 1
contador = 1  # Atribuições de variáveis necessarias para o cálculo.

# Lista para validação. Para saber se o número inserido pelo usuário consta ou não.
sequencia = []

# Começo da repetição para o cálculo
while contador <= num:
    terceiro = primeiro + segundo
    sequencia.append(terceiro)
    primeiro = segundo
    segundo = terceiro
    contador = contador + 1
# fim da repetição para o cálculo da sequência


print("-"*53)
if num in sequencia:
    print(f'O número "{num}" consta na sequência de Fibonacci.')
else:
    # bloco para verificar de o número inserito consta na lista.
    print(f'O número "{num}" não consta na sequência de Fibonacci.')


print("-"*53)
print(f'Sequência de Fibonacci completa: {sequencia}')  # Lista completa
