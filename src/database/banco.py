import sqlite3

def conectar():
    return sqlite3.connect("corridas.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS corridas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            distancia REAL,
            tarifa REAL,
            valor_km REAL,
            espera REAL,
            total REAL,
            data_hora TEXT
    )
""")
    
    conexao.commit()
    conexao.close()

def salvar_corrida(distancia, tarifa, valor_km, espera, total, data_hora):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO corridas (distancia, tarifa, valor_km, espera, total, data_hora)
        VALUES (?, ?, ?, ?, ?, ?)
""", (distancia, tarifa, valor_km, espera, total, data_hora))

    conexao.commit()
    conexao.close()

def lista_corridas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM corridas ORDER BY id DESC")
    dados = cursor.fetchall()

    conexao.close()
    return dados

