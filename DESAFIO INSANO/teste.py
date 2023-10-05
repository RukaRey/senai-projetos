import openpyxl

# Abra um arquivo Excel existente
workbook = openpyxl.load_workbook('cadastro.xlsx')

# Acesse a planilha padrão (Sheet 1)
sheet = workbook.active

sheet['A2'] = 'Alice'
sheet['B2'] = 25

# Salve o arquivo
workbook.save('cadastro.xlsx')

# Leia dados das células
nome = sheet['A2'].value
idade = sheet['B2'].value

print(f'Nome: {nome}, Idade: {idade}')

# Itere sobre as linhas e imprima os dados
for row in sheet.iter_rows(min_row=2, max_row=3, min_col=1, max_col=2):
    nome, idade = [cell.value for cell in row]
    print(f'Nome: {nome}, Idade: {idade}')
