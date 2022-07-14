"""
cores = ['amarelo', 'verde', 'vermelho', 'azul']
print(cores)

curso = 'Programação em Python: Essencial'

print(curso)

cores.append('azul')

print(cores)

cores.clear()
print(cores)

"""
# Definindo a primeira função
# Definição da função
def diz_oi():
	print('Oi!')

"""
Observação:
1. Veja que , dentro das nossas funções podemos utilizar outras funções.
2. Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que faz é dizer oi:
3. Veja que esta função não recebe nenhum parametro de entrada.
3. Veja que esta função não retorna nada.
"""

# Chamada de execução
diz_oi()
"""
Atenção:
Nunca esqueça de utilizar o parênteses antes de executar uma função.

"""
def cantar_parabens():
	print('parabens pra voce')
	print('nessa data querida')
	print('muitas felicidades')
	print('muitos anos de vida')
	print('viva ao aniversáriamente...')

"""
for n in range(5):
	print(n)
	cantar_parabens()
"""
# Em Python podemos inclusive criar variáveis do tipo de uma função e executar esta função através da variável
canta = cantar_parabens
canta()