import tkinter as tk

#Configuração da janela
janela = tk.Tk()
janela.title("Calculadora de Taxi")
janela.geometry("300x300")
janela.resizable(False, False)

#Configurando as contas
def calcular():
    print("O botao foi clicado")


#Distancia
lbDistancia = tk.Label(janela, text="Distancia (KM): ")
lbDistancia.pack(pady=(10,0))

EtDistancia = tk.Entry(janela, width= 40)
EtDistancia.pack()

#Valor inicial
lbtarifa = tk.Label(janela, text="Tarifa inicial:")
lbtarifa.pack(pady=(10,0))

Ettarifa = tk.Entry(janela, width= 40)
Ettarifa.pack()

#Valor por KM
lbKm = tk.Label(janela, text="Valor por KM:")
lbKm.pack(pady=(10,0))

EtKM = tk.Entry(janela, width= 40)
EtKM.pack()

#Valor por espera
lbTempo = tk.Label(janela, text="Valor por espera (Opcional):")
lbTempo.pack(pady=(10,0))

EtTempo = tk.Entry(janela, width= 40)
EtTempo.pack(pady=(10,0))

#Botao para calcular  (Sem Funçao)
bntCalcular = tk.Button(janela, text="Calcular", command=calcular)
bntCalcular.pack(pady=20)

#Resultado
resultado_label = tk.Label(janela, text="Total da corrida: R$ 0.00")
resultado_label.pack()

#Obrigatorio para que a janela fique rodando!
janela.mainloop()
