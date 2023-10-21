# imports
import math
import numpy as np
import sympy as sp

class Retas():
  def __init__(self):
    self.ponto_r1 = 0
    self.ponto_r2 = 0
    self.vetor_r1 = 0
    self.vetor_r2 = 0
    
  def setV1(self, vetor_r1):
    self.vetor_r1 = vetor_r1

  def setV2(self, vetor_r2):
    self.vetor_r2 = vetor_r2
    
  def setP1(self, ponto_r1):
    self.ponto_r1 = ponto_r1
    
  def setP2(self, ponto_r2):
    self.ponto_r2 = ponto_r2
  
  def equacao_vetorial(self):
    '''
    Pega os ponto da reta 1 e reta 2 somado para a 
    multiplicação de t para o vetor da reta 1 e reta 2
    '''
    equacao_vetorial = f'{self.ponto_r1} + t * {self.vetor_r1}'
    equacao_vetorial2 = f'{self.ponto_r2} + t * {self.vetor_r2}'
    
    return equacao_vetorial, equacao_vetorial2

  def equacao_parametrica(self):
    '''
    Definimos as variaveis h e t usadas nas equações para fazer os sistemas:
     - ponto da reta 1 + h * vetor da reta 1
     - ponto da reta 2 + t * vetor da reta 2
    '''
    h, t = sp.symbols('h t')

    a = sp.Matrix(self.ponto_r1) + h * sp.Matrix(self.vetor_r1)
    b = sp.Matrix(self.ponto_r2) + t * sp.Matrix(self.vetor_r2)

    return a, b

  def is_paralelas(self):
    '''
    Verificação das retas para saber se elas são paralelas:
      - Basta fazer a divisão de (a / d), (b / e), (c / f)
      - Após a divisão verificar se elas tem os valores iguais.
      - Valores iguais são paralelas, se não forem iguais não são paralelas
    '''
    a = self.vetor_r1[0] / self.vetor_r2[0]
    b = self.vetor_r1[1] / self.vetor_r2[1]
    c = self.vetor_r1[2] / self.vetor_r2[2]
    
    return a == b and b == c
  
  def is_coincidentes(self):
    '''
    Verifica se as retas são  paralelas coincidentes:
      - Para isso ela deve ser paralela e tem-se que fazer o calulo de a, b, c.
      - Calculo: 
        (x0 - x1) / d
        (y0 - y1) / e
        (z0 - z1) / f
    '''
    if self.is_paralelas():
      a = (self.ponto_r1[0] - self.ponto_r2[0]) / self.vetor_r2[0]
      b = (self.ponto_r1[1] - self.ponto_r2[1]) / self.vetor_r2[1]
      c = (self.ponto_r1[2] - self.ponto_r2[2]) / self.vetor_r2[2]
      
      return a == b and b == c
    return False

  def is_distintas(self):
    '''
    Verifica se as retas são paralelas distintas:
      - Basta verificar se ela é paralela e não e coincidente.
    '''
    if self.is_paralelas() and not self.is_coincidentes():
      return True
    return False
  
  def is_concorrentes(self):
    '''
    Verificação das retas para ver se elas são concorrentes:
      - Faz um sistema com duas variaveis (h, t) para que assim possa achar o valor das mesmas.
      - Calcula-se o valor de z0 e z1 com os valores de h e t. 
      - Se z0 = z1: São concorrentes.
      - Pode-se pegar o ponto de interseção e o ângulo sendo que elas são concorrentes.
    '''
    h, t = sp.symbols('h t')

    equacao1 = sp.Eq(self.vetor_r1[0] * h - self.vetor_r2[0] * t, self.vetor_r2[0] - self.vetor_r1[0])
    equacao2 = sp.Eq(self.vetor_r1[1] * h - self.vetor_r2[1] * t, self.vetor_r2[1] - self.vetor_r1[1])
    solucao_sistema = sp.solve((equacao1, equacao2), (h, t))
    
    try:   
      valor_h = solucao_sistema[h]
      valor_t = solucao_sistema[t]
    except:
      return False, None, None, None, None, None, None
    
    z0 = self.ponto_r1[2] + self.vetor_r1[2] * valor_h
    z1 = self.ponto_r2[2] + self.vetor_r2[2] * valor_t
    
    if z0 != z1: return False

    intersecao = self.pegar_intersecao_concorrente(valor_h)
    angulo = self.calcula_angulo_concorrentes()
    return True, valor_h, valor_t, z0, z1, intersecao, angulo

  def produto_escalar(self):
    '''
    Produto escalar entre dois vetores:
      - O produto escalar resulta em um valor inteiro.
    '''
    solucao = 0
    
    for i, j in zip(self.vetor_r1, self.vetor_r2):
      solucao += i * j

    return math.fabs(solucao)
  
  def calcula_angulo_concorrentes(self):
    '''
    Calcula o ângulo que se encontra entre as retas:
      - Através da função: cos^(-1) (abs(u * v))) / (abs(vet(u)) * abs(vet(v)))
    '''
    return math.acos(self.produto_escalar() / (self.modulo(self.vetor_r1) * self.modulo(self.vetor_r2)))
  
  def modulo(self, v):
    '''
    Função usada para fazer o modulo de um vetor (v).
    '''
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
  
  def pegar_intersecao_concorrente(self, valor_h):
    '''
    Pegar o ponto de interseção das retas concorrentes:
      - Para isso basta pegar as equações parametricas de alguma reta e substituir o valor de t
      - Após isso você irá achar o (x, y, z) -> PONTO DE INTERSEÇÃO
    '''
    h = sp.Symbol('h')
    
    a, _ = self.equacao_parametrica()
    equacoes_resolvidas = []

    for equacao in a:
      equacoes_resolvidas.append(equacao.subs(h, valor_h))
      
    return equacoes_resolvidas

  def is_reverso(self):
    '''
    Verificação das retas caso sejam reversas:
      - Para serem reversas basta elas não serem paralelas nem concorrentes.
    '''
    return not self.is_paralelas() and not self.is_concorrentes()
