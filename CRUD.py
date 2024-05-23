import mysql.connector
import pandas as pd
import os

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
        comando = 'SELECT * FROM vendedores'
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
        comando = 'DELETE FROM vendedores WHERE nome = %s'
        valores = (self.nome,)
        cursor.execute(comando, valores)
        conexao.commit()

    def exportToExcel(self, file_path):
        comando = 'SELECT * FROM vendedores'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        colunas = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(resultado, columns=colunas)
        df.to_excel(file_path, index=False)
        print(f"Dados exportados para {file_path}")

    def importFromExcel(self, file_path):
        if not os.path.exists(file_path):
            print(f"Arquivo não encontrado: {file_path}")
            return
        df = pd.read_excel(file_path)
        for index, row in df.iterrows():
            comando_select = 'SELECT cpf FROM vendedores WHERE cpf = %s'
            cursor.execute(comando_select, (row['cpf'],))
            resultado = cursor.fetchone()
            if resultado:
                comando_update = '''
                    UPDATE vendedores 
                    SET nome = %s, data_nascimento = %s, email = %s, estado = %s 
                    WHERE cpf = %s
                '''
                valores = (row['nome'], row['data_nascimento'], row['email'], row['estado'], row['cpf'])
                cursor.execute(comando_update, valores)
            else:
                comando_insert = '''
                    INSERT INTO vendedores (nome, cpf, data_nascimento, email, estado) 
                    VALUES (%s, %s, %s, %s, %s)
                '''
                valores = (row['nome'], row['cpf'], row['data_nascimento'], row['email'], row['estado'])
                cursor.execute(comando_insert, valores)
        conexao.commit()
        print(f"Dados do arquivo {file_path} foram importados e atualizados no banco de dados")

print(f"Current directory: {os.getcwd()}")

####Exemplos de Uso#######
'''
vendedor = Vendedor()
vendedor.exportToExcel('vendedores.xlsx')
vendedor.importFromExcel('C:/Users/Marcos/PycharmProjects/pythonProject/vendedores.xlsx')
'''
'''
vendedor = Vendedor()
vendedor.post('marcos', '11110989997', '2001/09/09', 'marcos@gmail.com', 'SP')
vendedor.updateEmailByName('marcos', 'marcosnovoemail@gmail.com' )
vendedor.deleteByName('marcos')
vendedor.getVendedores()
'''




