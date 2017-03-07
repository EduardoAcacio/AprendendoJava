import oauth2
import json
import urllib.parse
import pprint

arquivo = open('extraction.txt', 'w')

consumer_key = 'QgxgOzyKlF1kKlx3sP69KRbJW'
consumer_secret = '1hHFxPoCCFimemSUu6eziRYrEBSYEv0vhOvNIuqs0qICMG6lPi'

token_key = '93712144-wnj2djv5ADqOnNNcLVXQTckrEf0p1lygL3zLA2pRT'
token_secret = 'vfpNdt6At4Oed3o57XmLgXMQrZjoTRLvOCJk7g3NGo3Vp'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

query = input("Pesquisa: ")
query_cod = urllib.parse.quote(query, safe='')
print(' ')
requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_cod)

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)
twittes = objeto['statuses']

a = 0
while a <= 10:
    for twit in twittes:
        a += 1

        b = twit['user']['screen_name']
        c = twit['user']['name']
        d = twit['user']['description']
        e = twit['user']['url']
        f = twit['user']['created_at']
        g = twit["text"]
        h = twit['created_at']

        print(a)
        print(twit['user']['screen_name'])
        print(twit['user']['name'])
        print(twit['user']['description'])
        print(twit['user']['url'])
        print(twit['user']['created_at'])
        print(twit["text"])
        print(twit['created_at'])
        print()
        lista = {a, b, c, d, e, f, g, h}
        arquivo.write(str(lista))

'''b = twit['user']['screen_name']
c = twit['user']['name']
d = twit['user']['description']
e = twit['user']['url']
f = twit['user']['created_at']
g = twit["text"]
h = twit['created_at']

lista = {a, b, c, d, e, f, g, h}
arquivo.write(str(lista))'''


