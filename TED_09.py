clubes = []
for i in range(5):
    nome = input(f'Escreva o nome de 5 clubes e futebol: ')
    clubes.append(nome)

clube = input('Digite o nome do time que deseja buscar: ')
if clube in clubes :
    print('ACHEI')
else:
    print('NAO ACHEI')