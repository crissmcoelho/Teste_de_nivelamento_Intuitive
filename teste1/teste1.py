# Importando bibliotecas necessárias

from PyPDF2 import PdfMerger
from zipfile import ZipFile

#Criando uma lista com todos os anexos

list_anexos = ('Anexo1.pdf', 'Anexo2.pdf')

merger = PdfMerger()

# Criando um loop para acessar todos os arquivos da lista
for list in list_anexos:
    merger.append(list)
      
merger.write('todos_os_anexos.pdf') 
print('Todos os arquivos foram mergeados com sucesso!')

#Compactação dos arquivos
with ZipFile('todos_os_arquivos.zip', 'w') as zip:
    zip.write('todos_os_anexos.pdf')   
    
    print('Arquivos zipados com sucesso!')
    zip.close()
