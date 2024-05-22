import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Estagio123',
    database='crud',
)
cursor = conexao.cursor()

class Vendedor:
    # POST/CREATE
    def post(self, nome, cpf, data_nascimento, email, estado):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.email = email
        self.estado = estado
        comando = "INSERT INTO vendedores (nome, cpf, data_nascimento, email, estado) VALUES (%s, %s, %s, %s, %s)"
        valores = (self.nome, self.cpf, self.data_nascimento, self.email, self.estado)
        cursor.execute(comando, valores)
        conexao.commit()


vendedor = Vendedor()

vendedor.post('marcos', '11110989997', '2001/09/09', 'marcos@gmail.com', 'SP')

'''
    #GET/READ
    comando = f'SELECT * FROM vendedores'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)

    #PUT/UPDATE
    comando = f'UPDATE vendedores SET email = ("novoemail@gmail.com") WHERE nome = "João"'
    cursor.execute(comando)
    conexao.commit()
    #DELETE
    comando = f'DELETE FROM vendedores WHERE nome = "João"'
    cursor.execute(comando)
    conexao.commit()
'''
