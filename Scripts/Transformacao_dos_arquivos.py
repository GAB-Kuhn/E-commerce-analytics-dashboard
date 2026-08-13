import pandas as pd

# Pagina de vendas, cada planilha 
d_2024 = pd.read_excel('Vendas_ECommerce_2024.xlsx', sheet_name='Vendas_2024')
d_2025 = pd.read_excel('Vendas_ECommerce_2025.xlsx', sheet_name='Vendas_2025')
d_2026 = pd.read_excel('Vendas_ECommerce_2026.xlsx', sheet_name='fVendas')


lista_vendas = [d_2024, d_2025, d_2026]

colunas_padrao_venda = [
    'ID_Venda', 
    'Data_Venda', 
    'ID_Cliente', 
    'ID_Produto', 
    'Quantidade', 
    'Valor_Unitario', 
    'Valor_Total']

for df in lista_vendas:
    df.columns = colunas_padrao_venda

juncao_vendas = pd.concat(lista_vendas, ignore_index=True)

#Pagina clientes 

c_clientes_2024 = pd.read_excel ('Vendas_ECommerce_2024.xlsx',sheet_name='Cadastro_Clientes')
c_clientes_2025 = pd.read_excel ('Vendas_ECommerce_2025.xlsx', sheet_name='Clientes')
c_clientes_2026 = pd.read_excel ('Vendas_ECommerce_2026.xlsx', sheet_name='dClientes')

c_clientes = [c_clientes_2026, c_clientes_2025, c_clientes_2024]

colunas_padrao_clientes = [
    'ID_Cliente',
    'Nome_Cliente',
    'Estado_UF',
    'Regiao',
    'Data_Cadastro',]

print (c_clientes_2024.columns)

for df in c_clientes:
    df.columns = colunas_padrao_clientes

print (c_clientes_2024.columns)

juncao_clientes = pd.concat(c_clientes, ignore_index=True).drop_duplicates(subset=['ID_Cliente'])

#Pagina de produtos

p_produtos_2024 = pd.read_excel ('Vendas_ECommerce_2024.xlsx',sheet_name='Catalogo_Produtos')
p_produtos_2025 = pd.read_excel ('Vendas_ECommerce_2025.xlsx', sheet_name='Produtos')
p_produtos_2026 = pd.read_excel ('Vendas_ECommerce_2026.xlsx', sheet_name='dProdutos')

p_produtos = [p_produtos_2026, p_produtos_2025, p_produtos_2024]

colunas_padrao_produtos = [
    'ID_Produto',
    'Nome_Produto',
    'Categoria',
    'Preco_Tabela']

for df in p_produtos:
    df.columns = colunas_padrao_produtos

juncao_produtos = pd.concat(p_produtos, ignore_index=True).drop_duplicates(subset=['ID_Produto'])

#Junção de todas as planilhas em uma só

with pd.ExcelWriter('Vendas_ECommerce_completo.xlsx') as writer:
    juncao_vendas.to_excel(writer, sheet_name='Vendas', index=False)
    juncao_clientes.to_excel(writer, sheet_name='Clientes', index=False)
    juncao_produtos.to_excel(writer, sheet_name='Produtos', index=False)
