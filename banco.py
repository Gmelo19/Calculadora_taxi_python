import sqlite3

def conectar():
    return sqlite3.connect("conectar.db")

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursos.execute("""
        CREATE TABLE IF NOTE EXISTS corrida (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            distacia REAL,
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
