import tkinter as tk
from calculo import calcular_frete

#importando banco
from banco import criar_tabela, salvar_corrida
criar_tabela()

from datetime import datetime

def salvarbd():
    try:
        distancia = float(EtDistancia.get())
        tarifa =  float(Ettarifa.get())
        valor_km = float(EtKM.get())
        espera = float(EtTempo.get() if EtTempo() else 0)

        total = calcular_frete(distancia, tarifa, valor_km, espera)
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        salvar_corrida(distancia, tarifa, valor_km, espera, total, data_hora)

        resultado_label.config(text="Corrida salva no banco!")

    except ValueError:
        resultado_label.config(text="ERRO: Preencha corretamente antes de salvar.")

#Configuração da janela
janela = tk.Tk()
janela.title("Calculadora de Taxi")
janela.geometry("400x300")
janela.resizable(False, False)

#Deixar tudo centralizado
janela.columnconfigure(0, weight=1)
janela.columnconfigure(0, weight=2)

#Configurando as contas
def calcular():
    print("O botao foi clicado")


#Distancia
lbDistancia = tk.Label(janela, text="Distancia (KM): ")
lbDistancia.grid(row=0, column=0, padx=10, pady=10, sticky="e")

EtDistancia = tk.Entry(janela, width= 40)
EtDistancia.grid(row=0, column=1, padx=10, pady=10, sticky="e")

#Valor inicial
lbtarifa = tk.Label(janela, text="Tarifa inicial:")
lbtarifa.grid(row=1, column=0, padx=10, pady=10, sticky="e")

Ettarifa = tk.Entry(janela, width= 40)
Ettarifa.grid(row=1, column=1, padx=10, pady=10)

#Valor por KM
lbKm = tk.Label(janela, text="Valor por KM:")
lbKm.grid(row=2, column=0, padx=10, pady=10, sticky="e")

EtKM = tk.Entry(janela, width= 40)
EtKM.grid(row=2, column=1, padx=10, pady=10)

#Valor por espera
lbTempo = tk.Label(janela, text="Valor por espera:")
lbTempo.grid(row=3, column=0, padx=10, pady=10, sticky="e")

EtTempo = tk.Entry(janela, width= 40)
EtTempo.grid(row=3, column=1, padx=10, pady=10)

def calcular():
    try:
        distancia = float(EtDistancia.get())
        tarifa = float(Ettarifa.get())
        valor_km = float(EtKM.get())
        espera = float(EtTempo.get()) if EtTempo.get() else 0

        total = calcular_frete(distancia, tarifa, valor_km, espera)

        resultado_label.config(text=f"Total da corrida: R$ {total:.2f}")

    except ValueError:
        resultado_label.config(text="ERRO: Preencha todos os campos com números.")

def limpar():
    EtDistancia.delete(0, tk.END)
    Ettarifa.delete(0, tk.END)
    EtKM.delete(0, tk.END)
    EtTempo.delete(0, tk.END)
    resultado_label.config(text="Total da corrida: R$ 0.00")

#Botao para calcular 
bntCalcular = tk.Button(janela, text="Calcular", command=calcular)
bntCalcular.grid(row=4, column=0, columnspan=2, pady=15)

#Botao limpar
botao_limpar = tk.Button(janela, text="Limpar Campos", command=limpar)
botao_limpar.grid(row=6, column=0, columnspan=2, pady=5)

botao_salvar_bd = tk.Button(janela, text="Salvar no Banco", command=salvarbd)
botao_salvar_bd.grid(row=8, column=0, columnspan=2, pady=5)

#Resultado
resultado_label = tk.Label(janela, text="Total da corrida: R$ 0.00")
resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

#Obrigatorio para que a janela fique rodando!
janela.mainloop()
