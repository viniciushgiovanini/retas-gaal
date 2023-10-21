# imports
import math
import numpy as np
import sympy as sp

class Retas():
  def __init__(self, ponto_r1, ponto_r2, vetor_r1, vetor_r2):
    self.ponto_r1 = ponto_r1
    self.ponto_r2 = ponto_r2
    self.vetor_r1 = vetor_r1
    self.vetor_r2 = vetor_r2
  
  def equacao_vetorial(self):
    # TODO: fix, fazer
    return None

  def equacao_parametrica(self):
    h, t = sp.symbols('h t')

    a = sp.Matrix(self.ponto_r1) + h * sp.Matrix(self.vetor_r1)
    b = sp.Matrix(self.ponto_r2) + t * sp.Matrix(self.vetor_r2)

    return a, b

  def is_paralelas(self):
    a = self.vetor_r1[0] / self.vetor_r2[0]
    b = self.vetor_r1[1] / self.vetor_r2[1]
    c = self.vetor_r1[2] / self.vetor_r2[2]
    
    return a == b and b == c
  
  def is_coincidentes(self):
    if self.is_paralelas():
      a = (ponto_r1[0] - ponto_r2[0]) / vetor_r2[0]
      b = (ponto_r1[1] - ponto_r2[1]) / vetor_r2[1]
      c = (ponto_r1[2] - ponto_r2[2]) / vetor_r2[2]
      
      return a == b and b == c
    return False

  def is_distintas(self):
    if not self.is_paralelas() and not self.is_coincidentes():
      return True
    return False
  
  def is_concorrentes(self):
    h, t = sp.symbols('h t')

    equacao1 = sp.Eq(vetor_r1[0] * h - vetor_r2[0] * t, vetor_r2[0] - vetor_r1[0])
    equacao2 = sp.Eq(vetor_r1[1] * h - vetor_r2[1] * t, vetor_r2[1] - vetor_r1[1])
    solucao_sistema = sp.solve((equacao1, equacao2), (h, t))
    valor_h = solucao_sistema[h]
    valor_t = solucao_sistema[t]
    
    z0 = ponto_r1[2] + vetor_r1[2] * valor_h
    z1 = ponto_r2[2] + vetor_r2[2] * valor_t

    print(f' h: {valor_h}\n t: {valor_t}\n')
    print(f' z0: {z0}\n z1: {z1}\n')
    
    if z0 != z1: return False

    print('interseção concorrente:\n', self.pegar_intersecao_concorrente(valor_h), '\n')
    print('ângulo:\n', self.calcula_angulo_concorrentes(), '\n')
    return True

  def produto_escalar(self):
    solucao = 0
    
    for i, j in zip(self.vetor_r1, self.vetor_r2):
      solucao += i * j

    return math.fabs(solucao)
  
  def calcula_angulo_concorrentes(self):
    return math.acos(self.produto_escalar() / (self.modulo(self.vetor_r1) * self.modulo(self.vetor_r2)))
  
  def modulo(self, v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
  
  def pegar_intersecao_concorrente(self, valor_h):
    h = sp.Symbol('h')
    
    a, _ = self.equacao_parametrica()
    equacoes_resolvidas = []

    for equacao in a:
      equacoes_resolvidas.append(equacao.subs(h, valor_h))
      
    return equacoes_resolvidas

  def is_reverso(self):
    return not self.is_paralelas() and not self.is_concorrentes()


ponto_r1 = [3, 1, 2]
vetor_r1 = [1, 2, -1]
ponto_r2 = [5, -3, 4]
vetor_r2 = [3, -2, 1]

retas = Retas(ponto_r1, ponto_r2, vetor_r1, vetor_r2)

print('equação vetorial:\n', retas.equacao_vetorial(), '\n')

a, b = retas.equacao_parametrica()
print('equação paramétrica:\n', a, '\n', b, '\n')

print('retas paralelas:\n', retas.is_paralelas(), '\n')

print('retas coincidentes:\n', retas.is_coincidentes(), '\n')

print('retas distintas:\n', retas.is_distintas(), '\n')

print('retas concorrentes:\n', retas.is_concorrentes(), '\n')

print('retas reversas:\n', retas.is_reverso(), '\n')
