# imports
import math
import numpy as np
from sympy import symbols, Eq, solve


class equacao_reta():
  
  def vetorial(self, u, v):
    listaVetorialResultado = list(map(lambda x,y: y+x, u, v))
    return listaVetorialResultado
      
  def produto_escalar(self, u, v):
    prod_escalar = list(map(lambda x,y: x* y, u, v))
    return prod_escalar
  
  def modulo(self, u):
    modulo = list(map(lambda x: (x**2),u ))
    modulo = round(math.sqrt(sum(modulo)), 4)
  
    
  def equacao_vetorial_reta(self, vetor, ponto):
    
    x,y,z,t = symbols('x y z t')
    
    equacao_vetorial =  Eq((x,y,z), ponto +  t * vetor)
    # array = np.array(eval(equacao_vetorial))
    print(equacao_vetorial)
    return equacao_vetorial
  
  def equacao_parametrica_reta(self, vetor, ponto):
    # parametrica = ponto[0] + t * (vet[0])
    
    equacao_parametrica_list = []
    
    for each in ponto:
      
      tmp = 1 * vetor[0]
      
      string_tmp = f"{each} + "
    
    pass
  
  
vetor = [2,-3,5]
ponto = [1,2,-1]

obj = equacao_reta()
a = obj.equacao_vetorial_reta(vetor, ponto)
print(a)


