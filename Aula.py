contatos = {
    'Marcos' :'55549999099',
    'Maria' :'55549013312'
}

#ADD outro elemento
contatos['Pedro'] = "555492344234"
contatos['Marcos'] = "555492344234"
try:
    del contatos['Marias']
except:
    print("Contato não encontrado")
del contatos['Marias']
print(contatos)