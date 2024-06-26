<h1>
    Teste técnico
</h1>
<p>
  1. Crie uma classe para gerenciar vendedores (todas as funções de um CRUD -
Create, Read, Update e Delete).<br>
a. Considere pelo menos os seguintes atributos: Nome, CPF, data de
nascimento, e-mail e estado (UF).<br>
    <strong> Arquivo -> CRUD.py </strong><br>
    <strong> Instruções para rodar o CRUD: </strong><br>
    - Crie um banco de dados em root com o nome 'crud'<br>
    - Altere no código o login e a senha conforme seu usuário e senha do MySQL<br>
    - Rode o seguinte script SQL para criar a tabela vendedores: <br>
    <strong>
        CREATE TABLE vendedores (<br>
  id INT AUTO_INCREMENT PRIMARY KEY,<br>
  nome VARCHAR(255) NOT NULL,<br>
  cpf VARCHAR(11) NOT NULL UNIQUE,<br>
  data_nascimento DATE NOT NULL,<br>
  email VARCHAR(255) NOT NULL UNIQUE,<br>
  estado VARCHAR(2) NOT NULL<br>
);<br>
    </strong>
    Dentro do CRUD criei as quatro funções, sendo elas: <strong>post, getVendedores, updateEmailByName e deleteByName</strong>. Resolvi criar a função update somente para atualizar o email dos vendedores através do nome pois o email é o único atributo que pode sofrer mudança dentre nome, cpf, data de nascimento e estado. <br>
    No final do arquivo deixei exemplos de uso comentados para teste. Sendo eles: <br>
    vendedor = Vendedor()
    vendedor.post('marcos', '11110989997', '2001/09/09', 'marcos@gmail.com', 'SP')<br>
    vendedor.updateEmailByName('marcos', 'marcosnovoemail@gmail.com' )<br>
    vendedor.deleteByName('marcos')<br>
    vendedor.getVendedores()<br>
<br>


    2. Uma função para realizar a leitura de uma planilha com dados dos
vendedores para adicionar ou atualizar em lote.<br>
a. Considere o CPF como chave para a atualização.<br>
Ainda dentro do arquivo <strong>CRUD.py</strong> criei duas funções: a função <strong>exportToExcel()</strong>, que exporta a tabela do BD para um arquivo .xlsx, e a função <strong>importFromExcel()</strong> que realiza a leitura da planilha e atualiza os dados dos vendedores.
Deixei no final um exemplo comentado para teste: <br>
vendedor = Vendedor()<br>
vendedor.exportToExcel('vendedores.xlsx')<br>
vendedor.importFromExcel('C:/Users/Marcos/PycharmProjects/pythonProject/vendedores.xlsx')<br>
<br>
3. Uma função para realizar a leitura de uma planilha de vendas (ex:
https://docs.google.com/spreadsheets/d/1F8KUo66P5pQ1MKTPxU39li5S75rhAT
Sy4C5EMNcJNOc/edit?usp=sharing) e calcular as comissões que devem ser
pagas para cada vendedor. Considere as seguintes regras para as
comissões:<br>
a. Cada vendedor recebe 10% do valor de cada venda como comissão.<br>
b. Se a venda foi realizada por um canal online, 20% da comissão<br>
destinada ao vendedor é direcionada para a equipe de marketing.<br>
c. Se o valor total das comissões do vendedor for maior ou igual a R$
1.000,00, 10% da comissão é destinada ao gerente de vendas.<br>
Para solução, criei outro arquivo Python nomeado de <strong>Comissões.py</strong>, nele eu criei uma função que lê a planilha utilizando pandas, converte o atributo 'Valor da Venda' para o tipo numérico e depois realiza o cálculo de comissões do vendedor, da equipe de marketing e do gerente de vendas. <br>
Ao final deixei este exemplo de uso comentado: <br>
comissoes = calcular_comissoes()<br>
print(comissoes)<br>
<br>

4. Apresentar o volume de vendas (R$) e média por profissional para cada
canal e por cada estado.<br>
Para solução, criei um arquivo nomeado <strong>Volume_e_media.py</strong>, nele criei uma função uma função que lê a planilha utilizando pandas, converte o atributo 'Valor da Venda' para o tipo numérico e calcula o volume de vendas e a média por profissional para cada canal de venda. <br>
Ao final deixei este exemplo de uso comentado: <br>
volume_e_media_canal = volume_e_media_por_canal()<br>
print(volume_e_media_canal) <br>

<h2> TESTES </h2>
Por fim, no restante do meu tempo hábil para realização do desafio criei o arquivo <strong>test_vendedor.py</strong> para realizar testes para a classe Vendedor. Segue abaixo o que cada teste desenvolvido faz:<br>
<strong>setUpClass</strong>: Método de classe que configura a conexão com o banco de dados e cria a tabela de teste. <br>
<strong>tearDownClass</strong>: Método de classe que limpa a tabela de teste após todos os testes serem executados e fecha a conexão com o banco de dados.<br>
<strong>setUp</strong>: Método que limpa a tabela antes de cada teste individual para garantir um estado limpo.<br>
<strong>test_post</strong>: Testa a inserção de um novo vendedor.<br>
<strong>test_get_vendedores</strong>: Testa a obtenção de todos os vendedores.<br>
<strong>test_update_email_by_name</strong>: Testa a atualização do email de um vendedor pelo nome.<br>
<strong>test_delete_by_name</strong>: Testa a exclusão de um vendedor pelo nome.<br>
<strong>test_export_to_excel</strong>: Testa a exportação de dados para um arquivo Excel.<br>
<strong>test_import_from_excel</strong>: Testa a importação de dados de um arquivo Excel para o banco de dados.<br>

</p>
