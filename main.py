import requests

cep = input("Qual cep deseja consultar?")

cep = cep.replace("-","").replace(" ","")

url = f'https://viacep.com.br/ws/{cep}/json/'


response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    logradouro = data ['logradouro']
    complemento = data ['complemento']
    uf = data['uf']
    cidade = data['localidade']
    bairro = data['bairro']

    print (data)

else:
    print ("Erro de conexão")