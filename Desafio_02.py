n1= int(input('Digite um número para calcular sua tabuada: '))
arquivo = 'tabuada.txt'

with open(arquivo, 'w') as arquivo:
    arquivo.write(f'Tabuada do {n1}\n')
    for i in range(1,11):
        resultado = n1 * i
        linha = (f'{n1} x {i} = {resultado}\n')
        print(linha)
        arquivo.write(linha)