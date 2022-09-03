import requests

cep = input('CEP: ')

link = f'https://viacep.com.br/ws/{cep}/json/'

requisicao =  requests.get(link)

# print (type(requisicao.json()))
dic_requisicao = requisicao.json()

uf = dic_requisicao['uf']
cidade = dic_requisicao['localidade']

print ('ESTADO: ',uf,'\nCIDADE: ', cidade)
