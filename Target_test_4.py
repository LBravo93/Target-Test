# import sleep para adicionar um tempo entra as duas impressôes finais
from time import sleep

# atribuição da variável
alfabeto = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,Y,X,Z"

# Mostrando os resultados
print(alfabeto)
sleep(1)

# usei o len() para saber o fim da str, e o -1 para printar de trás para frente, até o final da str.
print(alfabeto[len(alfabeto)::-1])
