#ver o que está no databse  
import sqlite3
import os

# Caminho para o banco de dados
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, 'escola.db')

def listar_tabelas():
    """Lista todas as tabelas no banco de dados escola.db"""
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Query para listar todas as tabelas
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tabelas = cursor.fetchall()
        
        print("Tabelas encontradas no banco 'escola.db':")
        print("-" * 40)
        
        if tabelas:
            for tabela in tabelas:
                print(f"- {tabela[0]}")
        else:
            print("Nenhuma tabela encontrada.")
            
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
    except FileNotFoundError:
        print(f"Arquivo de banco de dados não encontrado: {DATABASE_PATH}")

def visualizar_estrutura_tabela(nome_tabela):
    """Visualiza a estrutura de uma tabela específica"""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        cursor.execute(f"PRAGMA table_info({nome_tabela});")
        colunas = cursor.fetchall()
        
        print(f"\nEstrutura da tabela '{nome_tabela}':")
        print("-" * 50)
        print("Coluna | Tipo | Null | Default | PK")
        print("-" * 50)
        
        for coluna in colunas:
            print(f"{coluna[1]} | {coluna[2]} | {'Não' if coluna[3] else 'Sim'} | {coluna[4] or 'N/A'} | {'Sim' if coluna[5] else 'Não'}")
            
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Erro ao acessar a tabela: {e}")

if __name__ == "__main__":
    listar_tabelas()
    
    # Para visualizar a estrutura de uma tabela específica (descomente a linha abaixo)
    visualizar_estrutura_tabela("alunos") 
    visualizar_estrutura_tabela("cursos") 
    visualizar_estrutura_tabela("matriculas")
    
    

