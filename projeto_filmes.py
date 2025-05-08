import time
from loguru import logger

bd_filmes = []

def cadastra_filmes(bd , titulo, ano):
    filme = [titulo, ano]
    bd.append(filme)
    return bd

def lista_filmes(bd):
    logger.info('Listagem de Filmes')
    for i in range(len(bd)):
        print(f'{i+1} | {bd[i][0]} | {bd[i][1]}')

def altera_filme(bd, indice, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd
def salvar_filmes(bd):
    
    with open('bd_filmes.txt', 'w', encoding='utf-8') as arquivo:
        for i in range(len(bd)):
            logger.info(f'Salvando o filme {bd[i][0]}')
            arquivo.write(f'{bd[i][1]},{bd[i][0]}\n')

while True:
    print('1 - Cadastrar Filme')
    print('2 - Listar Filmes')
    print('3 - Alterar Filme')
    print('4 - Salvar Filmes')
    try:
        op = int(input('Digite sua opção: '))
    except Exception as e:
        logger.error(f'Erros: {e}')
        logger.info('Digite um valor numérico!')
        op = -1

    if op == 1:
        logger.info('Iniciando um cadastro de filme')

        titulo = input('Digite o título do filme: ')
        ano = int(input('Digite o ano do filme: '))
        bd_filmes = cadastra_filmes(
            bd=bd_filmes,
            titulo=titulo,
            ano=ano,
        )

        logger.info('Filme cadastrado com sucesso')

    elif op == 2:
        logger.info('Iniciando listagem de filmes')
        lista_filmes(bd_filmes)
        logger.info('Filmes Listados')
    elif op == 3:
        logger.info('Iniciando a alteração do filme')
        lista_filmes(bd_filmes)
        i = int(input('Qual filme deseja alterar? '))
        titulo = input('Qual novo título? ')
        ano = int(input('Qual o novo ano? '))
        bd_filmes = altera_filme(
            bd=bd_filmes,
            indice=(i-1),
            ano=ano,
            titulo=titulo
        )

        logger.info('Filme Alterado')

    elif op == 4:
        logger.info('Iniciando persistência dos filmes')
        salvar_filmes(bd_filmes)
        logger.info('Filmes salvos com sucesso')
    else:
        print(f'Opção {op} inváçida')

    time.sleep(1)
