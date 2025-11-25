import tkinter as tk
from tkinter import ttk
from calculo import calcular_frete
from datetime import datetime
from reportlab.pdfgen import canvas
import os

# IMPORTS AJUSTADOS PARA NOVA ESTRUTURA
from api.api_rotas import geocodificar, calcular_TD
from database.banco import lista_corridas, criar_tabela, salvar_corrida

# Criar tabela no banco
criar_tabela()

# Caminho correto para PDF (agora na pasta data/pdfs)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_PDFS = os.path.join(BASE_DIR, "data", "pdfs")

if not os.path.exists(PASTA_PDFS):
    os.makedirs(PASTA_PDFS)

# -----------------------
# Função – Rota Real
# -----------------------
def calcular_rota_real():
    try:
        origem = EtOrigem.get()
        destino = EtDestino.get()

        lat_o, lon_o = geocodificar(origem)
        lat_d, lon_d = geocodificar(destino)

        distancia_km, tempo_min = calcular_TD((lat_o, lon_o), (lat_d, lon_d))

        resultado_label.config(
            text=f"Distância real: {distancia_km:.2f} km\nTempo estimado: {tempo_min:.1f} min"
        )

        EtDistancia.delete(0, tk.END)
        EtDistancia.insert(0, f"{distancia_km:.2f}")

    except Exception as e:
        resultado_label.config(text=f"Erro: {e}")

# -----------------------
# Salvar no Banco
# -----------------------
def salvarbd():
    try:
        distancia = float(EtDistancia.get())
        tarifa = float(Ettarifa.get())
        valor_km = float(EtKM.get())
        espera = float(EtTempo.get() or 0)

        total = calcular_frete(distancia, tarifa, valor_km, espera)
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        salvar_corrida(distancia, tarifa, valor_km, espera, total, data_hora)

        resultado_label.config(text="Corrida salva no banco!")

    except:
        resultado_label.config(text="Erro ao salvar no banco.")

# -----------------------
# Gerar PDF
# -----------------------
def gerar_pdf():
    try:
        distancia = float(EtDistancia.get())
        tarifa = float(Ettarifa.get())
        valor_km = float(EtKM.get())
        espera = float(EtTempo.get() or 0)
        total = calcular_frete(distancia, tarifa, valor_km, espera)
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        nome_pdf = os.path.join(PASTA_PDFS, f"recibo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
        pdf = canvas.Canvas(nome_pdf)

        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(180, 800, "RECIBO DE CORRIDA")

        pdf.setFont("Helvetica", 12)
        y = 760

        campos = [
            f"Distância: {distancia:.2f} km",
            f"Tarifa Inicial: R$ {tarifa:.2f}",
            f"Valor por KM: R$ {valor_km:.2f}",
            f"Espera: R$ {espera:.2f}",
            f"Total: R$ {total:.2f}",
            f"Gerado em: {data_hora}",
        ]

        for campo in campos:
            pdf.drawString(50, y, campo)
            y -= 20

        pdf.save()
        resultado_label.config(text=f"PDF salvo em: {nome_pdf}")

    except:
        resultado_label.config(text="Erro ao gerar PDF.")

# -----------------------
# Histórico
# -----------------------
def ver_histórico():
    janela_hist = tk.Toplevel(janela)
    janela_hist.title("Histórico")
    janela_hist.geometry("700x400")
    janela_hist.configure(bg="#121212")

    frame = ttk.Frame(janela_hist)
    frame.pack(fill="both", expand=True)

    colunas = ("ID", "Distância", "Tarifa", "Valor/KM", "Espera", "Total", "Data/Hora")
    tabela = ttk.Treeview(frame, columns=colunas, show="headings")

    for c in colunas:
        tabela.heading(c, text=c)
        tabela.column(c, width=100, anchor="center")

    scroll = ttk.Scrollbar(frame, orient="vertical", command=tabela.yview)
    tabela.configure(yscrollcommand=scroll.set)

    tabela.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")

    for item in lista_corridas():
        tabela.insert("", "end", values=item)

# ----------------------------------------------------
# INTERFACE DARK COMPLETA
# ----------------------------------------------------

janela = tk.Tk()
janela.title("Calculadora de Táxi")
janela.geometry("800x750")
janela.configure(bg="#121212")
janela.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

# Barra Superior
header = tk.Frame(janela, bg="#1E1E1E", height=70)
header.pack(fill="x")

titulo = tk.Label(
    header,
    text="Calculadora de Táxi",
    bg="#1E1E1E",
    fg="#EEEEEE",
    font=("Segoe UI", 20, "bold")
)
titulo.pack(pady=15)

# Função para criar cards
def criar_card(master):
    shadow = tk.Frame(master, bg="#0D0D0D")
    shadow.pack(pady=15, padx=25, fill="x")

    card = tk.Frame(shadow, bg="#1E1E1E", bd=0)
    card.pack(padx=2, pady=2, fill="x")
    return card

# Botões com Hover
def add_hover(widget):
    def on_enter(e):
        widget.configure(style="BotaoHover.TButton")
    def on_leave(e):
        widget.configure(style="Botao.TButton")
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

style.configure(
    "Botao.TButton",
    background="#334a61",
    foreground="white",
    font=("Segoe UI", 11, "bold"),
    padding=8,
    borderwidth=0
)

style.configure(
    "BotaoHover.TButton",
    background="#334a61",
    foreground="white",
    font=("Segoe UI", 11, "bold"),
    padding=8
)

style.configure("TLabel", background="#1E1E1E", foreground="#EEEEEE")
style.configure("TEntry", fieldbackground="#2A2A2A", foreground="#FFFFFF")

# -----------------------
# SEÇÃO 1 – ENDEREÇOS
# -----------------------
card_end = criar_card(janela)

ttk.Label(card_end, text="Origem:").grid(row=0, column=0, padx=10, pady=7, sticky="e")
EtOrigem = ttk.Entry(card_end, width=50)
EtOrigem.grid(row=0, column=1, pady=7)

ttk.Label(card_end, text="Destino:").grid(row=1, column=0, padx=10, pady=7, sticky="e")
EtDestino = ttk.Entry(card_end, width=50)
EtDestino.grid(row=1, column=1, pady=7)

btn_rota = ttk.Button(card_end, text="Calcular Rota Real", style="Botao.TButton", command=calcular_rota_real)
btn_rota.grid(row=2, column=0, columnspan=2, pady=12)
add_hover(btn_rota)

# -----------------------
# SEÇÃO 2 – DADOS DA CORRIDA
# -----------------------
card_dados = criar_card(janela)

ttk.Label(card_dados, text="Distância (KM):").grid(row=0, column=0, padx=10, pady=7, sticky="e")
EtDistancia = ttk.Entry(card_dados, width=40)
EtDistancia.grid(row=0, column=1, pady=7)

ttk.Label(card_dados, text="Tarifa Inicial:").grid(row=1, column=0, padx=10, pady=7, sticky="e")
Ettarifa = ttk.Entry(card_dados, width=40)
Ettarifa.grid(row=1, column=1, pady=7)

ttk.Label(card_dados, text="Valor por KM:").grid(row=2, column=0, padx=10, pady=7, sticky="e")
EtKM = ttk.Entry(card_dados, width=40)
EtKM.grid(row=2, column=1, pady=7)

ttk.Label(card_dados, text="Valor de Espera:").grid(row=3, column=0, padx=10, pady=7, sticky="e")
EtTempo = ttk.Entry(card_dados, width=40)
EtTempo.grid(row=3, column=1, pady=7)

resultado_label = ttk.Label(card_dados, text="Total da corrida: R$ 0.00", font=("Segoe UI", 11))
resultado_label.grid(row=4, column=0, columnspan=2, pady=13)

# -----------------------
# SEÇÃO 3 – BOTÕES
# -----------------------
card_btn = criar_card(janela)

btn_calc = ttk.Button(
    card_btn,
    text="Calcular Total",
    style="Botao.TButton",
    command=lambda: resultado_label.config(
        text=f"Total da corrida: R$ {calcular_frete(float(EtDistancia.get()), float(Ettarifa.get()), float(EtKM.get()), float(EtTempo.get() or 0)):.2f}"
    )
)
btn_calc.pack(pady=6, fill="x")
add_hover(btn_calc)

btn_limpar = ttk.Button(
    card_btn,
    text="Limpar Campos",
    style="Botao.TButton",
    command=lambda: [
        EtDistancia.delete(0, tk.END),
        Ettarifa.delete(0, tk.END),
        EtKM.delete(0, tk.END),
        EtTempo.delete(0, tk.END),
        resultado_label.config(text="Total da corrida: R$ 0.00")
    ]
)
btn_limpar.pack(pady=6, fill="x")
add_hover(btn_limpar)

btn_salvar = ttk.Button(card_btn, text="Salvar no Banco", style="Botao.TButton", command=salvarbd)
btn_salvar.pack(pady=6, fill="x")
add_hover(btn_salvar)

btn_hist = ttk.Button(card_btn, text="Ver Histórico", style="Botao.TButton", command=ver_histórico)
btn_hist.pack(pady=6, fill="x")
add_hover(btn_hist)

btn_pdf = ttk.Button(card_btn, text="Gerar PDF", style="Botao.TButton", command=gerar_pdf)
btn_pdf.pack(pady=6, fill="x")
add_hover(btn_pdf)

janela.mainloop()
