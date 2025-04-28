#Crie um programa que peça ao usuário para inserir várias notas de um aluno e calcule a média. Utilize um loop para continuar pedindo notas até que o usuário digite um valor específico para encerrar a entrada (por exemplo, -1).
soma  = 0
cont = 0
nota = 0
while nota != -1:

    nota  = float(input('Digite a nota: '))
    if nota == -1:
        break
    else:
        soma += nota
        cont += 1


print(f"A média é {soma/cont}")

