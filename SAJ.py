import pyodbc
import time

# Repositório de variáveis
outros_num=[]
nunaoformato=[]
cont = 0
c=0
x=[]
dicionario = {}
usuarios = []
n_formatado = []
processo = []

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto_branco':'\033[7;33m'}
# conexão a base de dados
conn = pyodbc.connect(
    "Driver={SQL Server Native Client 11.0};"
    "Server=10.100.188.129\ISAJ01;"
    "Database=SPJTESTE;"
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
for usuario in range(0, 48, 3):
    usuarios.append(outros_num[usuario])
for num_formatado in range(1, 48, 3):
    n_formatado.append(outros_num[num_formatado])
for proc in range(2, 48, 3):
    processo.append(outros_num[proc])

print(usuarios)
print(n_formatado)
print(processo)



