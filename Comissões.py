import pandas as pd

def calcular_comissoes():
    # Lendo a planilha
    df = pd.read_excel('Vendas.xlsx')

    # Convertendo a coluna 'Valor da Venda' para o tipo numérico
    df['Valor da Venda'] = pd.to_numeric(df['Valor da Venda'], errors='coerce')

    # Calculando as comissões
    df['Comissao'] = df['Valor da Venda'] * 0.10
    df.loc[df['Canal de Venda'] == 'Online', 'Comissao'] *= 0.80  # Deduzindo 20% para equipe de marketing

    # Calculando o total de comissões para cada vendedor
    total_comissoes_vendedor = df.groupby('Nome do Vendedor')['Comissao'].sum().reset_index()

    # Calculando a comissão para o gerente de vendas
    total_comissoes_vendedor['Comissao_Gerente'] = total_comissoes_vendedor['Comissao'].apply(
        lambda x: 0.10 * x if x >= 1000 else 0)

    # Retornando o DataFrame com as comissões
    return total_comissoes_vendedor

# Executando a função e imprimindo o resultado
comissoes = calcular_comissoes()
print(comissoes)

