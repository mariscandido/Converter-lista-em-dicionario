def convert_list_dic():
    d = [('Hendrix' , '1942'),
    ('Allman' , '1946'),
    ('King' , '1925'),
    ('Clapton' , '1945'),
    ('Johnson' , '1911'),
    ('Berry' , '1926'),
    ('Vaughan' , '1954'),
    ('Cooder' , '1947'),
    ('Page' , '1944'),
    ('Richards' , '1943'),
    ('Hammett' , '1962'),
    ('Cobain' , '1967'),
    ('Garcia' , '1942'),
    ('Beck' , '1944'),
    ('Santana' , '1947'),
    ('Ramone' , '1948'),
    ('White' , '1975'),
    ('Frusciante', '1970'),
    ('Thompson' , '1949'),]

# gerar um dicionario a partir de uma lista
    dici = dict(d)

# criar uma dicionario vazio
    flipped = {} 

# faz um for onde 'k' = chave(nome) e 'v' = valor(ano) fazendo um dicionario inverso jogando o ano para a chave concatenando o nome e incluindo no valor   
    for k, v in dici.items():
        if v not in flipped:
            flipped[v] = [k]
        else:
            flipped[v].append(k)

# faz um for onde 'h' = chave(ano) e 'v' = valor(nome) imprimindo o mesmo 
    for h, g in flipped.items():
        print(str(h) + ' : ' + str(g).replace("['","").replace("', '", " ").replace("']", ""))

if __name__ == '__main__':
    convert_list_dic()