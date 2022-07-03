from random import randint
from time import sleep


# CRIAR FUNÇÃO DE GERAR MATRIZ COM OPÇÃO DE ESCOLHA DO USUÁRIO
def gerarmatriz():
    mat = list()
    print('=' * 40)
    # Validar as dimensões informadas (dimensões negativas são inválidas)
    linhas = colunas = valida = 0
    while valida == 0:
        linhas = int(input('Quantas linhas terá a matriz? '))
        colunas = int(input('Quantas colunas terá a matriz? '))
        if linhas > 0 and colunas > 0:
            valida = 1
        else:
            print('Considere informar apenas números inteiros e positivos')
    # Dar a opção de escolha no modo de criação da matriz
    criarmat = 0
    while criarmat != 1 and criarmat != 2:
        criarmat = int(input("""Como deseja montar a sua matriz?
    Valores Aleatórios = 1
    Digitar os Valores = 2
    """))
    # Criar a matriz de acordo com a escolha do usuário
    if criarmat == 1:
        for i in range(0, linhas):
            # criar linha vazia
            mat.append([])
            for j in range(0, colunas):
                # preencher matriz com valores aleatórios
                mat[i].append(float(randint(0, 10)))
    else:
        for i in range(0, linhas):
            mat.append([])
            for j in range(0, colunas):
                # prencher matriz com valores digitados pelo usuário
                mat[i].append(float(input(f'Digite a valor a ser adicionado na posição [{i + 1}:{j + 1}]: ')))
    print('Matriz Criada!')
    print('=' * 40)
    return mat


# CRIAR FUNÇÃO PRA EXIBIR A MATRIZ FORMATADA
def exibirmatriz(matriz):
    # Formatar e exibir a matriz na tela
    diml = len(matriz)
    dimc = len(matriz[0])
    print('=======' * dimc)
    for i in range(0, diml):
        for j in range(0, dimc):
            print(f'{matriz[i][j]:<7}', end='')
        print()
    print('=======' * dimc)


# CRIAR FUNÇÃO DE SOMAR MATRIZ
def somarmatriz(mat1, mat2):
    linm1 = len(mat1)
    colm1 = len(mat1[0])
    linm2 = len(mat2)
    colm2 = len(mat2[0])
    mats = list()
    # validar se as matrizes têm dimensões iguais
    if (linm1 == linm2) and (colm1 == colm2):
        for i in range(0, linm1):
            mats.append([])
            for j in range(0, colm1):
                mats[i].append(mat1[i][j] + mat2[i][j])
        print('Resultado das matrizes A+B:')
        exibirmatriz(mats)
    else:
        print('Erro!! As matrizes não podem ser somadas, pois não têm dimensões iguais!')


# CRIAR FUNÇÃO DE MULTIPLICAR MATRIZES
def multimatriz(mat1, mat2):
    colm1 = len(mat1[0])
    colm2 = len(mat2[0])
    linm2 = len(mat2)
    val = aux = 0
    multm = list()
    # validar tamanho das matrizes
    if colm1 == linm2:
        while aux < len(mat1):
            multm.append([])
            # multiplica os elementos da linha aux por todos os elementos de mat2
            for i in range(0, colm2):
                for j in range(0, linm2):
                    val += (mat1[aux][j]) * (mat2[j][i])
                multm[aux].append(val)
                val = 0
            aux += 1
        print('Resultado das matrizes AxB:')
        exibirmatriz(multm)
    else:
        print('Erro!! As matrizes não podem ser multiplicadas, dimensões imcompatíveis!')


# CRIAR FUNÇÃO DE TRANSPOR MATRIZES
def transpormat(matriz):
    linm = len(matriz)
    colm = len(matriz[0])
    matresult = list()
    # validar se a matriz é quadrada
    if linm == colm:
        for i in range(0, linm):
            matresult.append([])
            for j in range(0, colm):
                matresult[i].append(matriz[j][i])
        print('Matriz tranposta!')
        exibirmatriz(matresult)
    else:
        print('Erro! A matriz não pode ser transposta pois não é quadrada.')


# CRIAR FUNÇÃO DE ESCALONAR MATRIZES
# substituição retroativa
def retroativa(mat, b):
    dimm = len(mat)
    result = dimm * [0]
    for i in range(dimm - 1, -1, -1):
        soma = 0
        for j in range(i + 1, dimm):
            # f(X) = jX
            soma += mat[i][j] * result[j]
        result[i] = (b[i] - soma) / mat[i][i]
    return result


# tornar a matriz triangular
def escalonamat(mat, b):
    dima = len(mat)
    dimb = len(b)
# validar dimensão da matriz com os resultados informados
    if dima == dimb:
        for p in range(0, dima - 1):
            for i in range(p + 1, dima):
                # troca de linha caso pivô = 0
                if mat[p][p] == 0:
                    linha = mat[p]
                    mat[p] = mat[+1]
                    mat[p+1] = linha
                    troca = b[p]
                    b[p] = b[p+1]
                    b[p+1] = troca
                # inverso do elemento a ser zerado, divido pelo pivô
                inv = - mat[i][p] / mat[p][p]
                for j in range(p + 1, dima):
                    # altera os valores da linha
                    # L2 = L2 + inv * L1
                    mat[i][j] += inv * mat[p][j]
                # altera o elemento na coluna de resultados
                b[i] = b[i] + inv * b[p]
                # zera o elemento desejado
                mat[i][p] += inv * mat[p][p]
        r = retroativa(mat, b)
        return r
    else:
        return 'A matriz não corresponde com os valores de B'


# CORPO DO CÓDIGO
# exibir menu e receber resposta
exe = 0
matriz1 = list()
matriz2 = list()
while exe == 0:
    # Menu de opções.
    valid = 0
    menu = 0
    while valid == 0:
        menu = int(input("""
            ==================================
            Que ação deseja fazer?
            ==================================
            1 = Somar matrizes
            ----------------------------------
            2 = multiplicar matrizes
            ----------------------------------
            3 = transpor matriz
            ----------------------------------
            4 = escalonar matriz
            ----------------------------------
            5 = encerrar o programa
            ==================================
                       """))
        if (menu >= 1) and (menu <= 5):
            valid = 1
        else:
            print('Erro! O valor informado não corresponde a nenhuma ação! tente novamente.')
    if (menu >= 1) and (menu <= 2):
        control = 0
        while control == 0:
            if len(matriz2) == 0:
                # criar as matrizes
                print('Matriz A:')
                matriz1 = gerarmatriz()
                sleep(1)
                print('Matriz B:')
                matriz2 = gerarmatriz()
                sleep(1)
            else:
                while (menu < 1) or (menu > 4):
                    menu = int(input("""
                    Somar matrizes = 1
                    Multiplicar matrizes = 2
                    Gerar novas matrizes = 3
                    voltar ao menu anterior = 4
                    """))
            if menu == 1:
                # soma de matrizes
                print('Matriz A:')
                exibirmatriz(matriz1)
                sleep(1.5)
                print('Matriz B:')
                exibirmatriz(matriz2)
                sleep(1.5)
                somarmatriz(matriz1, matriz2)
                sleep(2.5)
            elif menu == 2:
                # multiplicação de matrizes
                print('Matriz A:')
                exibirmatriz(matriz1)
                sleep(1.5)
                print('Matriz B:')
                exibirmatriz(matriz2)
                sleep(1.5)
                multimatriz(matriz1, matriz2)
                sleep(2.5)
            elif menu == 3:
                print('Matriz A:')
                matriz1 = gerarmatriz()
                sleep(1)
                print('Matriz B:')
                matriz2 = gerarmatriz()
                sleep(1)
            elif menu == 4:
                control = 1
            menu = 0
    elif menu == 3:
        # transposição
        if len(matriz2) == 0:
            # transpor matriz independente
            matriz3 = gerarmatriz()
            print('matriz:')
            exibirmatriz(matriz3)
            print('Transpondo Matriz, aguarde', end='')
            for c in range(0, 3):
                print('.', end='')
                sleep(1)
            print()
            transpormat(matriz3)
            sleep(2)
        else:
            control = 0
            while control == 0:
                menu = 0
                while (menu < 1) or (menu > 4):
                    menu = int(input("""
                    Transpor matriz A = 1
                    Transpor matriz B = 2
                    Transpor matriz independente = 3
                    (A & B serão preservadas)
                    Voltar ao menu anterior = 4
                    """))
                if menu == 1:
                    # transpor A
                    print('Matriz A')
                    exibirmatriz(matriz1)
                    print('Transpondo Matriz A, aguarde', end='')
                    for c in range(0, 3):
                        print('.', end='')
                        sleep(1)
                    print()
                    transpormat(matriz1)
                    sleep(2)
                if menu == 2:
                    # transpor B
                    print('matriz B:')
                    exibirmatriz(matriz2)
                    print('Transpondo Matriz B, aguarde', end='')
                    for c in range(0, 3):
                        print('.', end='')
                        sleep(1)
                    print()
                    transpormat(matriz2)
                    sleep(2)
                if menu == 3:
                    # transpor matriz independente
                    print('Matriz C')
                    matriz3 = gerarmatriz()
                    print('matriz C:')
                    exibirmatriz(matriz3)
                    print('Transpondo Matriz C, aguarde', end='')
                    for c in range(0, 3):
                        print('.', end='')
                        sleep(1)
                    print()
                    transpormat(matriz3)
                    sleep(2)
                if menu == 4:
                    control = 1
    elif menu == 4:
        # escalonar
        # gerar matriz e validar dimensão quadrada
        control = 0
        esc = list()
        while control == 0:
            esc = gerarmatriz()
            if len(esc) == len(esc[0]):
                control = 1
            else:
                print('Por favor, informar apenas matriz quadrada')
        # gerar coluna de resultados
        res = list()
        control = 0
        while control != 1 and control != 2:
            control = int(input("""Como deseja declarar os termos independentes?
        Valores Aleatórios = 1
        Digitar os Valores = 2
        """))
        if control == 1:
            # gerar valores aleatórios
            for c in range(0, len(esc)):
                res.append(float(randint(1, 10)))
        else:
            for c in range(0, len(esc)):
                # ler valores pelo teclado
                res.append(float(input(f'Que valor deseja adicionar para linha {c + 1}? ')))
        # exibir matriz aumentada
        print('matriz aumentada: ')
        for L in range(0, len(esc)):
            for C in range(0, len(esc[0])):
                print(f'{esc[L][C]:^5}', end='')
            print(f'| {res[L]}')
        print('Escalonando matriz...')
        sleep(2)
        # chamar a função
        esc = escalonamat(esc, res)
        # exibir resultado
        print('Resultado da matriz escalonada:')
        for c in range(0, len(res)):
            print(f'X{c + 1} = {esc[c]}')
        sleep(2.5)
    elif menu == 5:
        # finalizar o programa
        exe = 1
        print('FIM!')
        print('Obrigado por usar nosso programa, volte sempre.')
