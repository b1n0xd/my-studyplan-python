"""
Funções com Parâmetro (de entrada)
- Funções que recebem dados para serem processados dentro da mesma;
 Se pensarmos em um software qualquer, geralmente temos:
 entrada -> processamento -> saida

 Se pensarmos em uma função, já sabemos que temos funções que:
 - Não possuem entrada.
 - Não possuem saída.
 - Possuem entrada mas não possuem saida
 - Não possuem entrada mas possuem saida.
"""


# Refatorando uma função

# def quadrado(numero):
# 	return numero ** 3
#
#
# print(quadrado(7))


# Funções podem ter vários parametros de entrada, ou seja podemos receber como entrada
# quantos parametros forem necessários. Eles são separados por virgula.


def soma(a, b):
	return a + b


def multiplica(num1, num2):
	return num1 * num2


def outra(num1, b):
	return (num1 * b)

print(soma(2, 5))
print(soma(10, 30))

print(multiplica(2, 5))
print(multiplica(10, 30))

print(outra(2, 5))
print(outra(10, 30))