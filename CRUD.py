import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Estagio123',
    database='crud',
)
cursor = conexao.cursor()

class Vendedor:
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

    def getVendedores(self):
        comando = f'SELECT * FROM vendedores'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        print(resultado)

    def updateEmailByName(self, nome, email):
        self.nome = nome
        self.email = email

        comando = 'UPDATE vendedores SET email = %s WHERE nome = %s'
        valores = (self.email, self.nome)
        cursor.execute(comando, valores)
        conexao.commit()
    def deleteByName(self, nome):
        self.nome = nome
        comando = f'DELETE FROM vendedores WHERE nome = %s'
        valores = (self.nome,)
        cursor.execute(comando, valores)
        conexao.commit()

vendedor = Vendedor()
#vendedor.post('marcos', '11110989997', '2001/09/09', 'marcos@gmail.com', 'SP')
#vendedor.updateEmailByName('João', 'marcosnovoemail@gmail.com' )
vendedor.deleteByName('João')
vendedor.getVendedores()




