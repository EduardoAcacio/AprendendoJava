'''

Codigo extrai dados do Twitter
@author: Eduardo Acacio

'''

import oauth2
import json
import urllib.parse

a = 0

print('===== Extraindo dados do Twitter com Python 3.4 =====\n')
print('Faça uma pesquiva e receba um arquivo .TXT com até 3.000 twittes')

consumer_key = ''
consumer_secret = ''

token_key = ''
token_secret = ''

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("\nPesquisa: ")
query_cod = urllib.parse.quote(query, safe='')
print(' ')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_cod)

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']

arquivo = open('Extraction - '+query+'.txt', 'w')
arquivo.write(str('===== FILE START =====\n\n'))
arquivo.write(str("Twitter data extration with Python 3.4 \n\nWritten by: Eduardo Acacio \n\n"))
arquivo.write(str("Search: "))
arquivo.write(str(query))
arquivo.write(str(' \n\n'))

### abaixo temos a variavel 'a' que foi declarada no inicio do codigo
### o while vai de 'a' que é inicializado com 0 até 2985
### porque 2985?
### cada vez que o 'for' é executado ele extrai 15 twittes, fazendo até o numero 2985 extraimos 3000 twittes

while a <= 2985:
    for twit in twittes:
        a += 1
        b = twit['user']['screen_name']
        c = twit['user']['name']
        d = twit['user']['url']
        e = twit['user']['created_at']
        f = twit["text"]
        g = twit['created_at']

        arquivo.write(str(a))
        arquivo.write(str(' \n'))
        arquivo.write(str('Date: '))
        arquivo.write(str(g))
        arquivo.write(str(' \n'))
        arquivo.write(str('User: '))
        arquivo.write(str(b))
        arquivo.write(str(' \n'))
        arquivo.write(str('Name: '))
        arquivo.write(ascii(c))
        arquivo.write(str(' \n'))
        arquivo.write(str('URL: '))
        arquivo.write(ascii(d))
        arquivo.write(str(' \n'))
        arquivo.write(str('Date RT: '))
        arquivo.write(str(e))
        arquivo.write(str(' \n'))
        arquivo.write(str('Text: '))
        arquivo.write(ascii(f))
        arquivo.write(str(' \n\n'))

print('===== Arquivo extraction.txt gerado com sucesso! =====')

arquivo.write(str('\n\n ===== END FILE ====='))
arquivo.close()
