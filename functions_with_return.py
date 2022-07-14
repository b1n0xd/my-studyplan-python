"""
Funções com retorno


"""
numeros = [1, 2, 3]

rest_pop = numeros.pop()
print(f'Retorno de pop: {rest_pop}')

rest_pr = print(numeros)

print(f'Retorno de print: {rest_pr}')

# Vamos refatorar está função para que ela retorne o valor
def quadrado_de_7():
	print(7 * 7)

ret = quadrado_de_7()

print(f'Retorno {ret}')