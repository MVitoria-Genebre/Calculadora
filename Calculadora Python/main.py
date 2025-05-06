import sympy as sy
from sympy.interactive import init_printing
init_printing(pretty_print=True)

#-----------DERIVADA DA FUNÇÃO--------------
#DECLARANDO A VARIAVEL SIMBOLICA
x = sy.Symbol('x')
#EXPLICITANDO A FUNÇÃO
funcao = x**10
#RESOLVENDO A FUNÇÃO
resultado = sy.diff(funcao)
resultado