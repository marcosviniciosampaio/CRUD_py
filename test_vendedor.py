# test_vendedor.py
import unittest
import mysql.connector
import pandas as pd
import os
from CRUD import Vendedor

class TestVendedor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Estagio123',
            database='crud',
        )
        cls.cursor = cls.conexao.cursor()
        cls.vendedor = Vendedor()

        # Cria a tabela de teste
        cls.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendedores (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(100),
                cpf VARCHAR(11) UNIQUE,
                data_nascimento DATE,
                email VARCHAR(100),
                estado VARCHAR(50)
            )
        ''')
        cls.conexao.commit()

    @classmethod
    def tearDownClass(cls):
        # Remove a tabela de teste após os testes
        cls.cursor.execute('DROP TABLE vendedores')
        cls.conexao.commit()
        cls.cursor.close()
        cls.conexao.close()

    def setUp(self):
        # Limpa a tabela antes de cada teste
        self.cursor.execute('DELETE FROM vendedores')
        self.conexao.commit()

    def test_post(self):
        self.vendedor.post('João', '12345678901', '1990-01-01', 'joao@example.com', 'SP')
        self.cursor.execute('SELECT * FROM vendedores WHERE cpf = %s', ('12345678901',))
        resultado = self.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], 'João')

    def test_get_vendedores(self):
        self.vendedor.post('Maria', '10987654321', '1992-02-02', 'maria@example.com', 'RJ')
        resultado = self.vendedor.getVendedores()
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0][1], 'Maria')

    def test_update_email_by_name(self):
        self.vendedor.post('Carlos', '10293847560', '1985-03-03', 'carlos@example.com', 'MG')
        self.vendedor.updateEmailByName('Carlos', 'novoemail@example.com')
        self.cursor.execute('SELECT email FROM vendedores WHERE nome = %s', ('Carlos',))
        resultado = self.cursor.fetchone()
        self.assertEqual(resultado[0], 'novoemail@example.com')

    def test_delete_by_name(self):
        self.vendedor.post('Ana', '98765432100', '1970-04-04', 'ana@example.com', 'BA')
        self.vendedor.deleteByName('Ana')
        self.cursor.execute('SELECT * FROM vendedores WHERE nome = %s', ('Ana',))
        resultado = self.cursor.fetchone()
        self.assertIsNone(resultado)

    def test_export_to_excel(self):
        self.vendedor.post('Luís', '11223344556', '1980-05-05', 'luis@example.com', 'SC')
        file_path = 'vendedores.xlsx'
        self.vendedor.exportToExcel(file_path)
        self.assertTrue(os.path.exists(file_path))
        df = pd.read_excel(file_path)
        self.assertEqual(len(df), 1)
        self.assertEqual(df.iloc[0]['nome'], 'Luís')
        os.remove(file_path)

    def test_import_from_excel(self):
        df = pd.DataFrame([{
            'nome': 'Paula',
            'cpf': '22334455667',
            'data_nascimento': '1995-06-06',
            'email': 'paula@example.com',
            'estado': 'PR'
        }])
        file_path = 'vendedores_import.xlsx'
        df.to_excel(file_path, index=False)
        self.vendedor.importFromExcel(file_path)
        self.cursor.execute('SELECT * FROM vendedores WHERE cpf = %s', ('22334455667',))
        resultado = self.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[1], 'Paula')
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()