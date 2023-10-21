import tkinter as tk
import tkinter.font as tkfont
from retas import Retas
from planos import Planos

#############################################
#                 METODOS - Uteis           #
#############################################

def centralizar_janela(janela):
    janela.update_idletasks()
    largura = janela.winfo_width()
    altura = janela.winfo_height()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry('{}x{}+{}+{}'.format(largura, altura, x, y))

def verificao(v1, v2, p1, p2):
    return len(v1) == 3 and len(v2) == 3 and len(p1) == 3 and len(p2) == 3


def convert(v1, v2, p1, p2):
    try:
        v1 = v1.get().split(',')
        value_V1 = [int(item.strip()) for item in v1]

        v2 = v2.get().split(',')
        value_V2 = [int(item.strip()) for item in v2]

        p1 = p1.get().split(',')
        value_P1 = [int(item.strip()) for item in p1]

        p2 = p2.get().split(',')
        value_P2 = [int(item.strip()) for item in p2]
        return value_V1, value_V2, value_P1, value_P2
    except:
        return False, False, False, False


def verificar_valores(v1, v2, p1, p2):
    if (v1):
        return verificao(v1, v2, p1, p2)
    return False


def set_retas(objReta, v1, v2, p1, p2):
    objReta.setV1(v1)
    objReta.setV2(v2)
    objReta.setP1(p1)
    objReta.setP2(p2)
    
    
def set_planos(objReta, ponto, vetor_normal, ponto_u, vetor_u):
    objReta.set_ponto(ponto)
    objReta.set_vetor_normal(vetor_normal)
    objReta.set_ponto_u(ponto_u)
    objReta.set_vetor_u(vetor_u)
    
####################################################
#             METODOS - Contas - Retas             #
####################################################


def equacao_vetorial(objReta, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_retas(objReta, v1, v2, p1, p2)
        vet_a, vet_b = objReta.equacao_vetorial()
        resp = f'Equação vetorial: \n {vet_a} \n {vet_b}'
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def equacao_parametrica(objReta, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        objReta.setV1(v1)
        objReta.setV2(v2)
        objReta.setP1(p1)
        objReta.setP2(p2)
        a, b = objReta.equacao_parametrica()
        resp = f'Equação paramétrica:\n {a} \n {b}'
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def retas_coincidentes(objReta, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_retas(objReta, v1, v2, p1, p2)
        resposta_coincidente = objReta.is_coincidentes()
        resp = "São coincidentes" if resposta_coincidente else "Não são coincidentes"
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def retas_paralelas(objReta, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_retas(objReta, v1, v2, p1, p2)
        resposta = objReta.is_paralelas()
        resp = "São paralelas" if resposta else "Não são paralelas"
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def retas_distintas(objReta, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_retas(objReta, v1, v2, p1, p2)
        resposta = objReta.is_distintas()
        resp = "São distintas" if resposta else "Não são distintas"
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def retas_concorrentes(objReta, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_retas(objReta, v1, v2, p1, p2)
        resposta_bool, h, t, z0, z1, intersecao, angulo = objReta.is_concorrentes()
        if resposta_bool:
            resp = f'É concorrente: \n h: {h} \n t: {t} \n z0: {z0} \n z1: {z1} \n intersecao: {intersecao} \n angulo: {angulo}'
        else:
            resp = 'Não é concorrente'
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def retas_reversas(objReta, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_retas(objReta, v1, v2, p1, p2)
        resposta = objReta.is_reverso()
        resp = "São reversas" if resposta else "Não são reversas"
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp

####################################################
#             METODOS - Contas - Planos            #
####################################################


def equacao_plano(objPlano, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_planos(objPlano, v1, v2, p1, p2)
        resp,_ = objPlano.equacao_plano()
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def planos_alfa(objPlano, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_planos(objPlano, v1, v2, p1, p2)
        resp = objPlano.alfa()
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def calcula_angulo_plano_reta(objPlano, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_planos(objPlano, v1, v2, p1, p2)
        resp = objPlano.calcula_angulo_plano_reta()
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def intersecao_reta(objPlano, v1, v2, p1, p2, txtCaixa):
    v1, v2, p1, p2 = convert(v1, v2, p1, p2)

    if (verificar_valores(v1, v2, p1, p2)):
        set_planos(objPlano, v1, v2, p1, p2)
        _,d = objPlano.equacao_plano()
        resp = str(objPlano.intersecao_reta(d))
    else:
        resp = "Valor invalido"
    txtCaixa["text"] = resp


def butoes(newWindowRetas, text, equacao, objReta, value_V1, value_V2, value_P1, value_P2, column, row, txtCaixa):
    button = tk.Button(newWindowRetas, text=text, command=lambda: equacao(
        objReta, value_V1, value_V2, value_P1, value_P2, txtCaixa), width=18)
    button.grid(column=column, row=row, pady=3, padx=3)


def caixa_texto(newWindowRetas, texto, column, row):
    label = tk.Label(newWindowRetas, text=texto)
    label.grid(column=column, row=row, pady=3, padx=3)
    texBox = tk.Entry(newWindowRetas)
    texBox.grid(column=column + 1, row=row, pady=3, padx=3)
    return texBox


def todos_botoes_retas(newWindowRetas, objReta, value_V1, value_V2, value_P1, value_P2, txtCaixa):
    butoes(newWindowRetas, "Equação vetorial", equacao_vetorial,
           objReta, value_V1, value_V2, value_P1, value_P2, 0, 0, txtCaixa)

    butoes(newWindowRetas, "Equação parametrica", equacao_parametrica,
           objReta, value_V1, value_V2, value_P1, value_P2, 0, 1, txtCaixa)

    butoes(newWindowRetas, "Retas paralelas", retas_paralelas,
           objReta, value_V1, value_V2, value_P1, value_P2, 0, 2, txtCaixa)

    butoes(newWindowRetas, "Retas coincidentes", retas_coincidentes,
           objReta, value_V1, value_V2, value_P1, value_P2, 0, 3, txtCaixa)

    butoes(newWindowRetas, "Retas distintas",  retas_distintas,
           objReta, value_V1, value_V2, value_P1, value_P2, 1, 0, txtCaixa)

    butoes(newWindowRetas, "Retas concorrentes", retas_concorrentes,
           objReta, value_V1, value_V2, value_P1, value_P2, 1, 1, txtCaixa)

    butoes(newWindowRetas, "Retas reversas", retas_reversas,
           objReta, value_V1, value_V2, value_P1, value_P2, 1, 2, txtCaixa)


def todos_botoes_planos(newWindowRetas, objReta, value_V1, value_V2, value_P1, value_P2, txtCaixa):
    #
    butoes(newWindowRetas, "Equação plano", equacao_plano,
           objReta, value_V1, value_V2, value_P1, value_P2, 0, 0, txtCaixa)

    butoes(newWindowRetas, "Angulo alfa", planos_alfa,
           objReta, value_V1, value_V2, value_P1, value_P2, 0, 1, txtCaixa)

    butoes(newWindowRetas, "Ângulo plano reta", calcula_angulo_plano_reta,
           objReta, value_V1, value_V2, value_P1, value_P2, 1, 0, txtCaixa)

    butoes(newWindowRetas, "Interseção da Reta", intersecao_reta,
           objReta, value_V1, value_V2, value_P1, value_P2, 1, 1, txtCaixa)

#############################################
#                 TELAS                     #
#############################################
def telas(titulo, obj, funcao, nome_v1, nome_v2, nome_p1, nome_p2):

    newWindow = tk.Tk()
    newWindow.title(titulo)

    # vet1
    value_V1 = caixa_texto(newWindow, nome_v1, 0, 4)
    # ve2
    value_V2 = caixa_texto(newWindow, nome_v2, 0, 5)
    # p1
    value_P1 = caixa_texto(newWindow, nome_p1, 0, 6)
    # p2
    value_P2 = caixa_texto(newWindow, nome_p2, 0, 7)

    bold_font = tkfont.Font(weight="bold", size=15)
    txt_resp = tk.Label(newWindow, text="Respostas", font=bold_font)
    txt_resp.grid(column=0, row=8, columnspan=2)

    txtCaixa = tk.Label(newWindow, width=30, height=10)
    txtCaixa.grid(column=0, row=9, pady=3, padx=3, columnspan=2)

    funcao(newWindow, obj, value_V1,
           value_V2, value_P1, value_P2, txtCaixa)

    newWindow.mainloop()


#############################################
#              MAIN INICIAL                 #
#############################################
def main():
  window = tk.Tk()
  window.geometry("300x400")

  window.title("Retas e Plano")

  centralizar_janela(window)
  
  bold_font = tkfont.Font(weight="bold", size=15)

  txt_orientacao = tk.Label(
      window, text="Selecione o tipo para começar", font=bold_font)
  txt_orientacao.grid(column=0, row=0, columnspan=2)

  objRetas = Retas()
  objPlano = Planos()

  buttonReta = tk.Button(window, text="Retas",
                        command=lambda: telas("Retas", objRetas, todos_botoes_retas, "Vetor 1", "Vetor 2", "Ponto 1", "Ponto 2"), padx=7, pady=7)
  buttonReta.grid(column=0, row=1, pady=10)
  buttonPlano = tk.Button(window, text="Planos",
                          command=lambda: telas("Planos", objPlano, todos_botoes_planos,"Vetor normal","Vetor reta","Ponto plano", "Ponto reta"), padx=7, pady=7)
  buttonPlano.grid(column=1, row=1, pady=10)

  window.mainloop()

if __name__ == '__main__':
  main()
