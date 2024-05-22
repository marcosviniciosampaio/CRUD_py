import pandas as pd

def volume_e_media_por_canal():
    # Lendo a planilha
    df = pd.read_excel('Vendas.xlsx')

    # Convertendo a coluna 'Valor da Venda' para o tipo numérico
    df['Valor da Venda'] = pd.to_numeric(df['Valor da Venda'], errors='coerce')

    # Calculando o volume de vendas e a média por profissional para cada canal de venda
    vendas_por_canal = df.groupby('Canal de Venda').agg(
        Volume_de_Vendas=('Valor da Venda', 'sum'),
        Media_por_Profissional=('Valor da Venda', lambda x: x.sum() / x.nunique())
    ).reset_index()

    # Retornando o DataFrame com o volume de vendas e a média por profissional para cada canal de venda
    return vendas_por_canal

# Executando a função e imprimindo o resultado
volume_e_media_canal = volume_e_media_por_canal()
print(volume_e_media_canal)
