import mysql.connector
from mysql.connector import Error
from models import criar_tabelas


def get_connection():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='agendai'
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar com o MySQL: {e}")
        return None

def testar_conexao():
    try:
        # Tenta se conectar apenas ao servidor, sem especificar o banco de dados
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )

        # Se a conexão com o servidor for bem-sucedida
        if conn.is_connected():
            print("Conexão com o servidor MySQL bem-sucedida!")

            # Verifica se o banco de dados 'agendai' existe
            cursor = conn.cursor()
            cursor.execute("SHOW DATABASES LIKE 'agendai'")
            database_exists = cursor.fetchone()

            if database_exists:
                print("O banco de dados 'agendai' já existe.")
                return True
            else:
                print("O banco de dados 'agendai' não foi encontrado. Por favor, crie-o.")
                criar_tabelas()
                return False

    except Error as e:
        # Se ocorrer um erro, ele será capturado aqui
        print(f"Erro ao conectar com o MySQL: {e}")
        return False

    finally:
        # Garante que a conexão seja fechada, mesmo se houver um erro
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("Conexão com o MySQL fechada.")

if testar_conexao():
    print("Você pode prosseguir com seu projeto!")
else:
    print("A conexão falhou. Verifique as credenciais ou a existência do banco de dados.")