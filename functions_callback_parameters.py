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


# def soma(a, b):
# 	return a + b
#
#
# def multiplica(num1, num2):
# 	return num1 * num2
#
#
# def outra(num1, b):
# 	return (num1 * b)
#
#
# print(soma(2, 5))
# print(soma(10, 30))
#
# print(multiplica(2, 5))
# print(multiplica(10, 30))
#
# print(outra(2, 5))
# print(outra(10, 30))

def nome_completo(nome, sobrenome):
	return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina0', 'Jolie'))


# A diferença entre Parâmetros e argumentos

# Parâmetros são variáveis declaras na definição de uma função.
# Argumentos são dados passados durante a execução de uma função.
# A ordem dos parâmetros importa.

# Argumentos nomeados (Keyword Arguments)

# Erro comum na utilização do return

def soma_impares(numeros):
	total = 0
	for num in numeros:
		if num % 2 != 0:
			total = total + num
	return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))