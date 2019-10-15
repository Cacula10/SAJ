import pyodbc

# Repositório de variáveis
lista=[]
#
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJHML;"
    "uid=saj;pwd=nltrecRephlcrA"
)
# Criação dos dois cursores para busca de Outros Numeros e Não formatado
cursor_out = conn.cursor()
cursor_nformat = conn.cursor()

# Guardando as variaveis
outnum = str(input('Digite um numero para busca: '))


#Concatenando com % para utilizar o like
outnum = '%' + outnum + '%'
#nformat = '%' + nformat + '%'

# Select do Banco
cursor_out.execute(" SELECT A.NUNAOFORMATADO, A.CDUSUINCLUSAO, B.CDPROCESSO, B.NUPROCESSO FROM SAJ.ESPJPROCOUTROSNUM AS A JOIN SAJ.ESPJPROCESSO AS B ON A.CDPROCESSO = B.CDPROCESSO WHERE A.NUNAOFORMATADO LIKE ?",outnum)

# Append na lista
for row in cursor_out:
    lista.append(row)

# exibindo os processos encontrados
if len(lista) > 20:
    continuar= str(input('O sistema encontrou mais que 20 processos com esse número você deseja exibi-los ? '))[0].upper()
    if continuar == 'S':
        print(lista)
        print()

continuar= str(input('Deseja continuar procurando ?'))

if continuar == 'N':
    print('FIM')
else:
    nformat = str(input('Digite um numero para uma nova busca'))



print('FIM')
