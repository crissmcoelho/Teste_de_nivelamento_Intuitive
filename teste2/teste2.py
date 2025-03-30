# Importando bibliotecas necessárias
from zipfile import ZipFile
import tabula 
import pandas as pd

# Função para substituir valores 
def replace_value(value):
    if value == 'OD':
        return 'Seg. Odontológica'
    elif value == 'AMB':
        return 'Seg. Ambulatorial'
    else:
        return value
    
#Conveter o arquivo em pdf em csv    
    
arquivo = tabula.read_pdf(r'C:\Users\criss\OneDrive\Área de Trabalho\Teste_de_nivelamento_Intuitive\teste2\Anexo1.pdf', pages= 'all')   
tabula.convert_into('Anexo1.pdf', 'Teste_Cristina_Coelho.csv', output_format = 'csv', pages= 'all')
pd.read_csv('Teste_Cristina_Coelho.csv', encoding = 'utf-8' )
print('Arquivos convertidos em csv com sucesso!')


#compactação do teste

with ZipFile('Teste_Cristina_Coelho.zip', 'w') as zip:
    zip.write('Teste_Cristina_Coelho.csv')   
    
    print('Arquivos zipados com sucesso!')
    zip.close()
