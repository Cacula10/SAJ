import pyodbc
# Repositório de variáveis

cont = 0
l_geral = [[], [], []]

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
num = str(input('Digite um numero para busca: '))
num = '%' + num + '%'

# Select's do Banco
cursor.execute("SELECT CDUSUINCLUSAO, NUNAOFORMATADO, CAST(NUPROCESSO AS VARCHAR) AS PROCESSO "
               "FROM ESPJPROCESSO WHERE NUPROCESSO LIKE ? OR NUNAOFORMATADO LIKE ?", num, num)



print(sum(cursor))
