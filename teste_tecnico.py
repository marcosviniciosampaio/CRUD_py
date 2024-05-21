import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Estagio123',
    database='crud',
)
cursor = conexao.cursor()
class Vendedor:
    #POST
    comando = f"INSERT INTO vendedores (nome, cpf, data_nascimento, email, estado) VALUES ('João', '11109890202', '2001/09/09', 'joao@gmail.com', 'SC')"
    cursor.execute(comando)
    conexao.commit()
    #GET
    comando = f'SELECT * FROM vendedores'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)