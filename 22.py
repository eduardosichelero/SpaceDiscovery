contatos = {
    'Marcos' :'55549999099',
    'Maria' :'55549013312'
}

#ADD outro elemento
contatos['Pedro'] = "555492344234"
contatos['Marcos'] = "555492344234"

print("Contatos")
for key, value in contatos.items():
    print(key, value)




print(contatos.pop('Marias',"Contato não encontrado"))
#Função .pop funciona da mesma maneira que try e except

print(contatos.get("Pedro","Contato não encontrado"))
#Função .get pega elemntos que não existem 

