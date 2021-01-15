# e^x -> exp(x)
# |x| -> abs(x)

import sympy as sy
from sympy.interactive import init_printing
from scipy import integrate
init_printing(pretty_print=True)

print("Possíveis Operações: \n - Limites; \n - Derivadas; \n - Integrais Indefinidas;")
operacoes = input("\nDigite o operação desejada: ")
variaveis = input("\nDigite quantas variáveis sua Função terá.\n(No máximo 3. Se 1 então use x, se 2 use x e y, se 3 use x, y e z): ")

if variaveis == '1':
  x = sy.symbols('x')
elif variaveis == '2':
  x, y = sy.symbols('x y')
elif variaveis == '3':
  x, y, z = sy.symbols('x y z')

funcao = input("\nDigite sua função: ")

if operacoes == "Limites" or operacoes == "limites":
  operacoes = input("\nLimites: No ponto, Laterais ou no Infinito")
  if operacoes == "No ponto" or operacoes == "no ponto":
    print("teste")
  elif operacoes == "Laterais" or operacoes == "laterais":
    limite = input("\nLimite em: ")
    if "Direita":
      limit(funcao,limite,0)
    elif "Esquerda":
      limit(funcao,limite,0,'-')
  elif operacoes == "No infinito" or operacoes == "no infinito":
    print("terste")

elif operacoes == "Derivadas" or operacoes == "derivadas":
  if variaveis != '1': derivar = input("\nDeseja derivar em função de qual variável? ")
  else: derivar = 'x'
  resultado = sy.diff(funcao, derivar) # Calcula o resultado da derivada parcial em funcao de X

elif operacoes == "Integrais Indefinidas" or operacoes == "integrais indefinidas":
  resultado = sy.integrate(funcao) # Calcula o resultado da integral indefinida


print("Resultado: ", resultado)