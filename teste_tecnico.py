import mysql.connector

class Vendedor:
    #conecta o banco de dados local:
    def conectar_banco(self):
        try:
            conexao = mysql.connector.connect(host="localhost",
                                              user="root",
                                              password="@Estagio123",
                                              database="crud")
            cursor = conexao.cursor()
            return conexao, cursor
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None, None

