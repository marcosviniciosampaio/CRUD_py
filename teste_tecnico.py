import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Estagio123',
    database='crud',
)
cursor = conexao.cursor()
class Vendedor:
    #POST/CREATE
    comando = f"INSERT INTO vendedores (nome, cpf, data_nascimento, email, estado) VALUES ('João', '11109890202', '2001/09/09', 'joao@gmail.com', 'SC')"
    cursor.execute(comando)
    conexao.commit()
    #GET/READ
    comando = f'SELECT * FROM vendedores'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
    #PUT/UPDATE
    comando = f'UPDATE vendedores SET email = ("novoemail@gmail.com") WHERE nome = "João"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados
    #DELETE
    comando = f'DELETE FROM vendedores WHERE nome = "João"'
    cursor.execute(comando)
    conexao.commit() # edita o banco de dados