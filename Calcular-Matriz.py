import numpy as np

# Desenvolvido por Ed Carlos da Silva Pereira

print('Calculadora de Matrizes')

decisao = int(input('Escolha a opção [2] 2x2, [3] 3x3, [4] 4x4: '))

if decisao == 2:
    linha1 = []
    linha2 = []

    print('Digite os valores da primeira linha')
    for c in range(0, 2):
        linha1.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))
    print('Digite os valores da segunda linha')
    for c in range(0, 2):
        linha2.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))

    matriz = []
    matriz.append(linha1)
    matriz.append(linha2)

    print('1 - Transposta')
    print('2 - Inversa')
    print('3 - Determinante')

    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        matrizCompleta = np.array(matriz)
        transposta = np.transpose(matrizCompleta)
        print('\nSua transposta é: {}'.format(transposta), end=' ')

    elif escolha == 2:
        matrizCompleta = np.array(matriz)
        inversa = np.linalg.inv(matrizCompleta)
        print('\nInversa da matriz é: {}'.format(inversa), end=' ')

    else:
        matrizCompleta = np.array(matriz)
        determinante = np.linalg.det(matrizCompleta)
        print('\n\nO determinante da matriz é: {}'.format(determinante))

elif decisao == 3:
    linha1 = []
    linha2 = []
    linha3 = []

    print('Digite os valores da primeira linha')
    for c in range(0, 3):
        linha1.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))
    print('Digite os valores da segunda linha')
    for c in range(0, 3):
        linha2.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))
    print('Digite os valores da terceira linha')
    for c in range(0, 3):
        linha3.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))

    matriz = []
    matriz.append(linha1)
    matriz.append(linha2)
    matriz.append(linha3)

    print('1 - Transposta')
    print('2 - Inversa')
    print('3 - Determinante')

    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        matrizCompleta = np.array(matriz)
        transposta = np.transpose(matrizCompleta)
        print('\nSua transposta é: {}'.format(transposta), end=' ')

    elif escolha == 2:
        matrizCompleta = np.array(matriz)
        inversa = np.linalg.inv(matrizCompleta)
        print('\nInversa da matriz é: {}'.format(inversa), end=' ')

    else:
        matrizCompleta = np.array(matriz)
        determinante = np.linalg.det(matrizCompleta)
        print('\n\nO determinante da matriz é: {}'.format(determinante))

else:
    linha1 = []
    linha2 = []
    linha3 = []
    linha4 = []

    print('Digite os valores da primeira linha')
    for c in range(0, 4):
        linha1.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))
    print('Digite os valores da segunda linha')
    for c in range(0, 4):
        linha2.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))
    print('Digite os valores da terceira linha')
    for c in range(0, 4):
        linha3.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))
    print('Digite os valores da quarta linha')
    for c in range(0, 4):
        linha4.append(int(input('Digite o valor da {}ª coluna: '.format(c + 1))))

    matriz = []
    matriz.append(linha1)
    matriz.append(linha2)
    matriz.append(linha3)
    matriz.append(linha4)

    print('1 - Transposta')
    print('2 - Inversa')
    print('3 - Determinante')

    escolha = int(input('Digite sua escolha: '))

    if escolha == 1:
        matrizCompleta = np.array(matriz)
        transposta = np.transpose(matrizCompleta)
        print('\nSua transposta é: {}'.format(transposta), end=' ')

    elif escolha == 2:
        matrizCompleta = np.array(matriz)
        inversa = np.linalg.inv(matrizCompleta)
        print('\nInversa da matriz é: {}'.format(inversa), end=' ')

    else:
        matrizCompleta = np.array(matriz)
        determinante = np.linalg.det(matrizCompleta)
        print('\n\nO determinante da matriz é: {}'.format(determinante))



















