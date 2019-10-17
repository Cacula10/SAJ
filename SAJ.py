import pyodbc
import time

# Repositório de variáveis
outros_num=[]
nunaoformato=[]
cont = 0

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto_branco':'\033[7;33m'}
# conexão a base de dados
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJHML;"
    "uid=saj;pwd=nltrecRephlcrA"
)
# Criação do cursor para busca do processo
cursor = conn.cursor()

# Guardando as variaveis e concatenando para uso do like no banco
proc = str(input('Digite um numero para busca: '))
proc = '%' + proc + '%'
time.sleep(0.5)

# Select's do Banco
cursor.execute("SELECT CDUSUINCLUSAO, NUNAOFORMATADO, CAST(NUPROCESSO AS VARCHAR) AS PROCESSO FROM ESPJPROCESSO WHERE NUPROCESSO LIKE ? OR NUNAOFORMATADO LIKE ?",proc,proc)
for row in cursor:
    outros_num.append(row[0].rstrip())
    outros_num.append(row[1])
    outros_num.append(row[2])
    cont += 1


print(format(cores['azul']))
print(("=>" * 20).format(""))
print('PROCURANDO')
print(("=>" * 20).format(""))
print(format(cores['limpa']))
time.sleep(2)

#  Exibição do usuário

print(outros_num)
