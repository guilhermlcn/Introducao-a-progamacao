palavra = input('Digite uma palavra: ')

def conta_vogais(v):

    vogais = 'aeiouAEIOU'
    qnt = 0
    for s in v:
        if s in vogais:
            qnt += 1
    return qnt

print('Sua palavra tem', (conta_vogais(f'{palavra}')))
