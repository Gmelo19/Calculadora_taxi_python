# 🚖 Calculadora de Frete para Táxi – Python (Tkinter + SQLite + API de Rotas)

Projeto desenvolvido para praticar Python aplicando interface gráfica (Tkinter), integração com API externa (OpenRouteService), cálculo automático de rotas reais e persistência de dados usando SQLite.

A aplicação calcula o valor de uma corrida de táxi com base em distância, tarifa inicial, valor por km, tempo parado e também permite obter a **distância real entre dois endereços** usando API externa.

---

## ✨ Funcionalidades

### 🖥 Interface gráfica moderna
- Desenvolvida com **Tkinter** e estilo personalizado (tema claro/escuro opcional)

### 🚗 Cálculo Completo da Corrida
- Distância (manual ou automática)
- Tarifa inicial
- Valor por KM
- Valor por espera (opcional)
- Total calculado

### 🌍 Consulta de Rota Real (API)
Integração com a API **OpenRouteService**:
- Converte endereços para latitude/longitude (geocoding)
- Calcula distância real
- Obtém tempo estimado de viagem
- Atualiza automaticamente o campo de distância

Endpoints utilizados:
- `/geocode/search`
- `/v2/directions/driving-car`

### 💾 Banco de Dados (SQLite)
Salva automaticamente cada corrida com:
- Distância
- Tarifas
- Espera
- Total final
- Data/Hora

### 📜 Histórico de Corridas
- Listado em uma nova janela
- Carregamento direto do banco

### 🧾 Geração de PDF
- Cria recibo da corrida
- Salva automaticamente na pasta `/data/pdfs`

---

## 📦 Estrutura do Projeto

    calculadora_taxi/
````│
├── run.py
├── requirements.txt
│
├── src/
│ ├── main.py
│ ├── calculo.py
│ │
│ ├── api/
│ │ └── api_rotas.py
│ │
│ ├── database/
│ │ └── banco.py
│ │
│ └── ui/
│ └── toplevel.py
│
└── data/
├── pdfs/
└── database/
````

---

## 🔧 Instalação e Execução

### 1️⃣ Instalar dependências:
```bash
pip install -r requirements.txt
```

2️⃣ Executar o programa:
- python run.py

## 🔑 Configurar API de Rotas

- Crie sua conta gratuita:
https://openrouteservice.org/
- Copie sua chave (API KEY)
- Cole no arquivo abaixo:
```API_KEY = "SUA_CHAVE_AQUI"```

## 🛣 Próximas Melhorias (Roadmap)

- Modo noturno/dark completo
- Gráfico dos valores das corridas
- Exportar histórico completo em PDF
- Integração com GPS no celular (APK futuramente)
- Layout 100% responsivo

---

## 👤 Autor
Gustavo Melo

Desenvolvedor Python Júnior
