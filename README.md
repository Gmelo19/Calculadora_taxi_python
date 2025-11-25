# 🚖 Calculadora de Táxi (Python + Tkinter)

Este é um projeto desenvolvido para praticar Python, Tkinter, organização de código e consumo de API externa.  
A aplicação calcula o valor de uma corrida de táxi, consulta a distância real entre dois endereços e salva os dados localmente.

---

## 🧰 Funcionalidades

- 🚗 Calcular distância real entre dois endereços  
- ⏱ Mostrar tempo estimado da viagem  
- 📏 Calcular valor total da corrida  
- 💾 Salvar corridas no banco de dados (SQLite)  
- 📊 Visualizar histórico de corridas  
- 📜 Gerar recibo PDF  
- 🎨 Interface moderna em Dark Mode  

---

## 🌐 API Utilizada: OpenRouteService

O projeto utiliza a **OpenRouteService**, uma API gratuita baseada no OpenStreetMap.

Ela é usada para:

- Converter endereço em latitude/longitude  
- Obter rota real de carro  
- Calcular distância em KM  
- Calcular tempo estimado em minutos  

### Endpoints utilizados:

/geocode/search
/v2/directions/driving-car


### Configurando a API:
Crie uma conta gratuita em:
https://openrouteservice.org/

Depois coloque sua chave no arquivo:
src/api/api_rotas.py


Linha:
''''python
API_KEY = "SUA_CHAVE_AQUI"





📂 Estrutura do Projeto
calculadora_taxi/
│
├── run.py
├── requirements.txt
│
├── src/
│   ├── main.py
│   ├── calculo.py
│   │
│   ├── api/
│   │   └── api_rotas.py
│   │
│   ├── database/
│   │   └── banco.py
│   │
│   └── ui/
│       └── toplevel.py
│
└── data/
    ├── pdfs/
    └── database/





▶ Como executar
Instalar dependências:
pip install -r requirements.txt

Rodar o programa:
python run.py

👤 Autor

Gustavo Melo
Desenvolvedor Python Júnior




