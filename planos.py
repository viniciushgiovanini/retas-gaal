# imports
import math
import numpy as np
import sympy as sp

class Planos():
    def __init__(self):
        self.ponto = 0
        self.vetor_normal = 0
        self.ponto_u = 0
        self.vetor_u = 0
    
    def set_ponto(self, ponto):
        self.ponto = ponto

    def set_vetor_normal(self, vetor_normal):
        self.vetor_normal = vetor_normal
        
    def set_ponto_u(self, ponto_u):
        self.ponto_u = ponto_u
        
    def set_vetor_u(self, vetor_u):
        self.vetor_u = vetor_u
        
    def equacao_plano(self):
        '''
        Mostra a equacao do plano.
            - Calcula-se d: d = -(aX0 + bY0 + cZ0)
            - Retorna a equacao da reta
        '''
        d = - self.vetor_normal[0] * self.ponto[0] - self.vetor_normal[1] * self.ponto[1] - self.vetor_normal[2] * self.ponto[2] 
        
        k = "+" if d > 0 else "-"
        equacao_plano = f'{self.vetor_normal[0]} * x + {self.vetor_normal[1]} * y + {self.vetor_normal[2]} * z {k} {math.fabs(d)} = 0'
        return equacao_plano, d

    def intersecao_reta(self, d):
        '''
        Pega o ponto de interseção das reta no plano:
            - a(x0 + d * t) + b(y0 + e * t) + c(z0 + f * t) + d = 0
            - Após achar a solução de t: substituia no sistema e você tem o ponto de interseção
        '''
        t = sp.Symbol('t')
        
        equacao = self.vetor_normal[0] * (self.ponto_u[0] + self.vetor_u[0] * t) + \
                  self.vetor_normal[1] * (self.ponto_u[1] + self.vetor_u[1] * t) + \
                  self.vetor_normal[2] * (self.ponto_u[2] + self.vetor_u[2] * t) + d
        
        equacao_t = sp.Eq(equacao, 0)
        solucao_t = sp.solve(equacao_t, t)[0]

        x = self.ponto_u[0] + self.vetor_u[0] * solucao_t
        y = self.ponto_u[1] + self.vetor_u[1] * solucao_t
        z = self.ponto_u[2] + self.vetor_u[2] * solucao_t
        
        return [x, y, z]

    def produto_escalar(self):
        '''
        Produto escalar entre dois vetores:
            - O produto escalar resulta em um valor inteiro.
        '''
        solucao = 0
        
        for i, j in zip(self.vetor_u, self.vetor_normal):
            solucao += i * j

        return math.fabs(solucao)
  
    def calcula_angulo_plano_reta(self):
        '''
        Calcula o ângulo que se encontra entre plano e reta:
            - Através da função: cos^(-1) (abs(u * n))) / (abs(vet(u)) * abs(vet(n)))
        '''        
        try:
          return math.acos(self.produto_escalar() / (self.modulo(self.vetor_u) * self.modulo(self.vetor_normal)))
        except:
          return 0
    def alfa(self):
        '''
        Calcula o angulo de alfa:
            - alfa = 90 - angulo_entre_plano_e_reta    
        '''
        
        return math.pi / 2 - self.calcula_angulo_plano_reta()
  
    def modulo(self, v):
        '''
    Função usada para fazer o modulo de um vetor (v).
    '''
        return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

# ponto = [4, 7, 9]
# vetor_normal = [1, 6, -5]
# ponto_u = [10, 3, -3]
# vetor_u = [14, 5, 2]

# planos = Planos(ponto, vetor_normal, ponto_u, vetor_u)

# eq, d = planos.equacao_plano()

# print('equação plano:\n', eq)

# print('interseção plano:\n', planos.intersecao_reta(d))

# print('calcula ângulo plano reta:\n', planos.calcula_angulo_plano_reta())

# print('alfa:\n', planos.alfa())
