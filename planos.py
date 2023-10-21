# imports
import math
import numpy as np
import sympy as sp

class Planos():
    def __init__(self, ponto, vetor_normal, ponto_u, vetor_u):
        self.ponto = ponto
        self.vetor_normal = vetor_normal
        self.ponto_u = ponto_u
        self.vetor_u = vetor_u
    
    def equacao_plano(self):
        '''
        P (x, y, z) -> Ponto qualquer no plano
        ax + by + cz + d = 0
        
        (a, b, c) -> normal
        
        d = -(aX0 + bY0 + cZ0)
        '''
    
        d = - self.vetor_normal[0] * self.ponto[0] - self.vetor_normal[1] * self.ponto[1] - self.vetor_normal[2] * self.ponto[2] 
        
        k = "+" if d > 0 else "-"
        equacao_plano = f'{self.vetor_normal[0]} * x + {self.vetor_normal[1]} * y + {self.vetor_normal[2]} * z {k} {math.fabs(d)} = 0'
        return equacao_plano, d

    def intersecao_reta(self, d):
        t = sp.Symbol('t')
        
        equacao = self.vetor_normal[0] * (self.ponto_u[0] + self.vetor_u[0] * t) + \
                  self.vetor_normal[1] * (self.ponto_u[1] + self.vetor_u[1] * t) + \
                  self.vetor_normal[2] * (self.ponto_u[2] + self.vetor_u[2] * t) + d
        
        equacao_t = sp.Eq(equacao, 0)
        solucao_t = sp.solve(equacao_t, t)[0]

        x = self.ponto_u[0] + self.vetor_u[0] * solucao_t
        y = self.ponto_u[1] + self.vetor_u[1] * solucao_t
        z = self.ponto_u[2] + self.vetor_u[2] * solucao_t
        
        return x, y, z

    def produto_escalar(self):
        solucao = 0
        
        for i, j in zip(self.vetor_u, self.vetor_normal):
            solucao += i * j

        return math.fabs(solucao)
  
    def calcula_angulo_plano_reta(self):
        return math.acos(self.produto_escalar() / (self.modulo(self.vetor_u) * self.modulo(self.vetor_normal)))

    def alfa(self):
        return math.pi / 2 - self.calcula_angulo_plano_reta()
  
    def modulo(self, v):
        return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

ponto = [1, 2, -1]
vetor_normal = [2, -1, 3]
ponto_u = [-1, 5, 3]
vetor_u = [2, 3, -1]

planos = Planos(ponto, vetor_normal, ponto_u, vetor_u)

eq, d = planos.equacao_plano()

print('equação plano:\n', eq)

print('interseção plano:\n', planos.intersecao_reta(d))

print('calcula ângulo plano reta:\n', planos.calcula_angulo_plano_reta())

print('alfa:\n', planos.alfa())
