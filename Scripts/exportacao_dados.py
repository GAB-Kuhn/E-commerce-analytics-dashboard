import pandas as pd
from sqlalchemy import create_engine

arquivo_principal = 'Vendas_ECommerce_completo.xlsx'

#Abrir sheet a sheet

vendas = pd.read_excel(arquivo_principal, sheet_name='Vendas')
clientes = pd.read_excel(arquivo_principal, sheet_name='Clientes')
produtos = pd.read_excel(arquivo_principal, sheet_name='Produtos')

engine = create_engine('mysql+pymysql://root:minhasenha@localhost:3306/ecommerce_db')

#Exportando os dados para o MySQL
vendas.to_sql('vendas', con=engine, index=False)
clientes.to_sql('clientes', con=engine, index=False)
produtos.to_sql('produtos', con=engine, index=False)

