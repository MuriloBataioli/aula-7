pessoas = {'fulano@gmail.com' : 'Fulano', 'ciclano@gmail.com' : 'ciclano'}

# para adiconar um nome no dicionario coloque
pessoas['zulano@gmail.com'] = 'Zulano'
#para remover é
del pessoas['ciclano@gmail.com']

#para deixar o usuario definir
email = input('Email: ')
nome = input('nome da pessoa: ')
pessoas[email] = nome

#para deixar o usuario decidir quem ele quer deletar
email2 = input('Email para remover: ')
del pessoas[email2]