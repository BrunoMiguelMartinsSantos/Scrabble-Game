# Fundamentos da Programação - 2.º Projeto
# Projeto: Jogo Scrabble
# Sou o Bruno Santos (ist1118057), aluno do 1.º ano da Licenciatura Bolonha em Engenharia Informática e de Computadores - Alameda.
# Email Pessoal: bruno793santos@gmail.com
# Email Institucional: bruno.martins.santos@tecnico.ulisboa.pt

LETRAS = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Z')
TAMANHO_DO_TABULEIRO = 15
PONTUACAO_DAS_LETRAS = {'A': 1, 'B': 3, 'C': 2, 'Ç': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 4, 'H': 4, 'I': 1, 'J': 5, 'L': 2, 'M': 1, 'N': 3, 'O': 1, 'P': 2, 'Q': 6, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'X': 8, 'Z': 8}

"""
TAD imutável casa: é usado para representar uma casa do tabuleiro de Scrabble.
Operações básicas associadas a TAD casa
"""

def cria_casa(lin, col):
    """
    Construtor:
    Recebe dois inteiros correspondentes à linha e coluna e devolve a casa correspondente.
    Verifica uma posição (linha, coluna) no tabuleiro e devolve o tuplo (l, c).
    Argumentos:
    lin --> Inteiro
    col --> Inteiro
    lin : Linha.
    col : Coluna.
    Returns:
    Retorna o tuplo (lin, col) que corresponde à casa do tabuleiro.
    """
    if not isinstance(lin, int) or not isinstance(col, int) or lin > TAMANHO_DO_TABULEIRO or col > TAMANHO_DO_TABULEIRO or col <= 0 or lin <= 0:
        raise ValueError('cria_casa: argumentos inválidos')
    return (lin, col)


def obtem_col(c):
    """
    Seletor:
    Devolve a coluna da casa.
    Argumentos:
    c --> Tuplo
    c: casa
    Returns:
    Retorna a coluna da casa.
    """
    return c[1]


def obtem_lin(c):
    """
    Seletor:
    Devolve a linha da casa.
    Argumentos:
    c --> Tuplo
    c: casa
    Returns:
    Retorna a linha da casa.
    """
    return c[0]


def eh_casa(arg):
    """
    Reconhecedor:
    Verifica se é uma casa válida.
    Argumentos:
    arg --> Universal
    Returns:
    Devolve True caso o seu argumento seja tuplo (linha, coluna) com inteiros entre 1 e TAMANHO_DO_TABULEIRO.
    Devolve False caso contrário.
    """
    return isinstance(arg, tuple) and len(arg) == 2 and type(arg[0]) == int and type(arg[1]) == int and arg[0] >= 1 and arg[0] <= 15 and arg[1] >= 1 and arg[1] <= 15


def casas_iguais(c1, c2):
    """
    Teste:
    Verifica se duas casas são iguais.
    Argumentos:
    c1 --> Universal
    c2 --> Universal
    Returns:
    Devolve True apenas se c1 e c2 são casas e são iguais, e False caso contrário.
    """
    return eh_casa(c1) and eh_casa(c2) and obtem_col(c1) == obtem_col(c2) and obtem_lin(c1) == obtem_lin(c2)


def casa_para_str(c):
    """
    Transformador:
    Devolve a cadeia de caracteres que representa a casa.
    Argumentos:
    c --> Tuple
    c: casa
    Returns:
    Devolve a cadeia de caracteres na forma '(l, c)'.
    """
    return '(' + str(obtem_lin(c)) + ',' + str(obtem_col(c)) + ')'


def str_para_casa(s):
    """
    Transformador:
    Devolve a casa correspondente à cadeia de caracteres.
    Argumentos:
    s --> String
    s: cadeia de caracteres que representa a casa
    Returns:
    Devove a casa correspondente à string.
    """
    conteudo = s.strip('()').split(',')  # remove os parênteses da string e separa os valores da linha e coluna por uma vírgula
    return (int(conteudo[0]), int(conteudo[1]))


"""Funções de alto nível associadas a TAD casa"""
def incrementa_casa(c, d, s):
    """  
    Argumentos:
    c --> casa
    d --> String
    d: direção
    s --> Inteiro
    d: distância 
    Returns:
    Devolve a casa dum tabuleiro de Scrabble a seguir da casa c na direção d e a distância s.
    Caso não exista, devolve a casa.
    """
    if not eh_casa(c) or d not in ('H', 'V') or type(s) != int or s <= 0:
        raise ValueError('incrementa_casa: argumentos inválidos')
    
    linha = obtem_lin(c)
    coluna = obtem_col(c)

    if d == 'H': # Move horinzontalmente na mesma linha
        nova_coluna = coluna + s
        if 1 <= nova_coluna and nova_coluna <= 15:
            return cria_casa(linha, nova_coluna) 
        else:
            return c # se sair fora do tabuleiro, mantém a casa original
        
    if  d == 'V': # Move vericalmente na mesma coluna
        nova_linha = linha + s
        if 1 <= nova_linha and nova_linha <= 15:
            return cria_casa(nova_linha, coluna)
        else:
            return c # se sair fora do tabuleiro, mantém a casa original
    

"""
TAD jogador é usado para representar um jogador do jogo Scrabble, a sua pontuação e letras. 
Os jogadores podem ser humanos ou agentes.
Operações básicas associadas a TAD jogador
"""
def cria_humano(nome):
    """
    Construtor:
    Cria o jogador humano do Scrabble.
    Argumentos:
    nome --> String
    nome: Representa o nome do jogador
    Returns:
    Devolve um dicionário que representa o jogador humano com 0 pontos e sem letras.
    """
    if nome.strip() == '' or not isinstance(nome, str):
        raise ValueError('cria_humano: argumento inválido')
    return {'nome': nome, 'pontos': 0, 'letras': [], 'identidade': 'Humano'}
        

def cria_agente(nivel):
    """
    Construtor:
    Cria o agente do Scrabble.
    Argumentos:
    nivel --> String
    nivel: Representa uma cadeia de carateres que corresponde ao nível do agente ('FACIL', 'MEDIO' ou 'DIFICIL')
    Returns:
    Devolve o jogador de Scrabble agente com 0 pontos e sem letras.
    """
    if nivel != 'FACIL' and nivel != 'MEDIO' and nivel != 'DIFICIL':
        raise ValueError('cria_agente: argumento inválido')
    return {'nivel': nivel, 'pontos': 0, 'letras': [], 'identidade': 'Agente'}


def jogador_identidade(j):
    """
    Seletor:
    Devolve o nome do jogador j se é um jogador humano ou o nível se é um jogador agente.
    Argumentos:
    j --> Jogador 
    Returns:
    Devolve o nome do jogador j se é um jogador humano ou o nível se é um jogador agente.
    """
    if j['identidade'] == 'Humano':
        return j['nome']
    if j['identidade'] == 'Agente':
        return j['nivel']
    

def jogador_pontos(j):
    """
    Seletor:
    Devolve os pontos do jogador j.
    Argumentos:
    j --> Jogador 
    Returns:
    Devolve os pontos do jogador j.
    """
    return j['pontos']


def jogador_letras(j):
    """
    Seletor:
    Devolve a cadeia de caracteres ordenadas com todas as letras do jogador j.
    Argumentos:
    j --> Jogador
    Returns:
    Devolve a cadeia de caracteres ordenadas com todas as letras do jogador j.
    """
    letras_ordenadas = sorted(j['letras'], key=lambda x: LETRAS.index(x))
    res = ''
    for letra in letras_ordenadas:
        res = res + letra
    return res


def recebe_letra(j, l):
    """
    Modificador:
    Modifica destrutivamente o jogador j acrescentado a letra l às suas letras.
    Argumentos:
    j --> Jogador
    l --> String
    Returns:
    Devolve o próprio jogador j.
    """
    j['letras'].append(l)
    return j


def usa_letra(j, l):
    """
    Modificador
    Modifica destrutivamente o jogador j retirando a letra l às suas letras.
    Argumentos:
    j --> Jogador
    l --> String
    l: letra l
    Returns:
    Devolve o próprio jogador j.
    """
    j['letras'].remove(l)
    return j


def soma_pontos(j, p):
    """
    Seletor
    Modifica destrutivamente o jogador j somando os pontos p à sua pontuação atual.
    Argumentos:
    j --> Jogador
    p --> String
    p: Pontos
    Returns:
    Devolve o próprio jogador j.
    """
    j['pontos'] = j['pontos'] + p
    return j


def eh_jogador(arg):
    """
    Reconhecedor:
    Verifica se um jogador é válido.
    Argumentos:
    arg --> Universal
    Returns:
    Devolve True caso o seu argumento seja um TAD jogador e False caso contrário.
    """
    return (isinstance(arg, dict) and 'identidade' in arg and arg['identidade'] in ('Humano', 'Agente') 
            and 'identidade' in arg and isinstance(arg['identidade'], str) and arg['identidade'].strip() != '' 
            and 'pontos' in arg and type(arg['pontos']) == int and 'letras' in arg and isinstance(arg['letras'], list))


def eh_humano(arg):
    """
    Reconhecedor:
    Verifica se o jogador é um humano.
    Argumentos:
    arg --> Universal
    Returns:
    Devolve True caso o seu argumento seja um TAD jogador humano e False caso contrário.
    """
    return eh_jogador(arg) and arg['identidade'] == 'Humano'


def eh_agente(arg):
    """
    Reconhecedor:
    Verifica se o jogador é um agente.
    Argumentos:
    arg --> 
    Returns:
    Devolve True caso o seu argumento seja um TAD jogador agente e False caso contrário.
    """
    return eh_jogador(arg) and arg['identidade'] == 'Agente'


def jogadores_iguais(j1, j2):
    """
    Teste:
    Testa se dois jogadores são iguais.
    Argumentos:
    j1 --> Universal
    j1: Jogador 1
    j2 --> Universal
    j2: Jogador 2
    Returns:
    Devolve True apenas se j1 e j2 forem jogadores.
    """
    if eh_jogador(j1) and eh_jogador(j2) and j1 == j2:
        return True
    else:
        return False
    

def jogador_para_str(t):
    """
    Transformador:
    Devolve a cadeia de caracteres que representa o jogador.
    Argumentos:
    t --> Jogador
    Returns:
    Devolve a cadeia de caracteres que representa o jogador.
    """
    letras = t['letras']
    letras_ordenadas = []
    i = 0
    while i < len(LETRAS):
        l = LETRAS[i]
        j = 0
        while j < len(letras):
            if letras[j] == l:
                letras_ordenadas = letras_ordenadas + [letras[j]]
            j = j + 1
        i = i + 1

    letras_str = '' # string final com as letras separadas por espaço
    i = 0
    while i < len(letras_ordenadas): # percorre todas as letras já ordenadas
        letras_str = letras_str + letras_ordenadas[i] # concatena a letra à string
        if i < len(letras_ordenadas) - 1:  # se não for a última, adiciona um espaço a seguir
            letras_str = letras_str + ' '
        i = i + 1

    pontos = t['pontos']
    if pontos < 10: # se for de um dígito, coloca um espaço à esquerda para alinhar com o formato pedido
        pontos_formatados = ' ' + str(pontos)
    else:
        pontos_formatados = str(pontos) # caso contrário, só a string do número

    # parte inicial antes da lista de letras
    if t['identidade'] == 'Humano':
        parte_inicial = t['nome'] + ' ( ' + pontos_formatados + '):'
    else:  # agente
        parte_inicial = 'BOT(' + t['nivel'] + ') ( ' + pontos_formatados + '):'

    # só acrescenta espaço se houver letras a seguir
    if letras_str != '':
        return parte_inicial + ' ' + letras_str
    return parte_inicial


"""
Funções de alto nível associadas a TAD jogador
"""
def distribui_letras(jog, saco, num):
    """
    Retira um máximo de num letras do final da lista saco (potencialmente vazia) e acrescenta-as ao jogador jog.
    A função modifica destrutivamente a lista de letras e o jogador passados como argumento.
    Argumentos:
    jog --> Jogador
    saco --> Lista
    num --> Inteiro
    Returns:
    Devolve o jogador.
    """
    total = len(saco)
    if num > total:
        num = total

    for i in range(num):
        letra = saco.pop()          # remove a última letra do saco
        jog = recebe_letra(jog, letra) # acrescenta ao jogador

    return jog

"""
TAD vocabulario: é usado para representar o conjunto de palavras que podem ser utilizadas durante o jogo
Operações básicas associadas a TAD vocabulario
"""
def cria_vocabulario(v):
    """
    Construtor:
    O tuplo contém pelo menos uma palavra e as palavras são cadeias de carateres. 
    As palavras são cadeias de caracteres únicas de letras maiúsculas do abecedário Português de comprimento entre 2 e 15 letras.
    Argumentos:
    v --> Tuplo
    v: vocabulário
    Returns:
    Devolve o vocabulário que contém as palavras contidas no tuplo.
    """
    if not isinstance(v, tuple) or len(v) == 0:
        raise ValueError('cria_vocabulario: argumento inválido')
    
    vocabulario = {}
    palavras_vistas = []

    i = 0
    while i < len(v):
        palavra = v[i]
        if not isinstance(palavra, str): #Verificar se é string
            raise ValueError('cria_vocabulario: argumento inválido')
        
        if len(palavra) < 2 or len(palavra) > 15: # Validar comprimento
            raise ValueError('cria_vocabulario: argumento inválido')
        
        # Validar letras
        j = 0
        while j < len(palavra):
            if palavra[j] not in LETRAS:
                raise ValueError('cria_vocabulario: argumento inválido')
            j = j + 1

        # Verificar se não há palavras repetidas
        if palavra in palavras_vistas:
            raise ValueError('cria_vocabulario: argumento inválido')
        palavras_vistas = palavras_vistas + [palavra]

        # Guardar a palavra dentro do vocabulário
        comprimento = len(palavra)
        inicial = palavra[0] # Obtem a primeira letra da palavra
        if comprimento not in vocabulario: # Verifica se já existe no dicionário vocabulario uma chave para esse comprimento
            vocabulario[comprimento] = {} # Se nao existir é criada
        if inicial not in vocabulario[comprimento]: # Dentro do grupo desse comprimento verifica se já existe uma entrada para a primeira letra
            vocabulario[comprimento][inicial] = [] # Adiciona a palavra à lista correspondente àquela primeira letra e comprimento.
        vocabulario[comprimento][inicial] = vocabulario[comprimento][inicial] + [palavra] # Cria uma nova lista com a palavra adicionada no fim
        i = i + 1
    
    return vocabulario


def obtem_pontos(vocabulario, palavra):
    """
    Seletor:
    Devolve os pontos da palavra do vocabulário.
    Argumentos:
    vocabulario --> vocabulário
    palavra --> String
    palavra: palavra
    Returns:
    Devolve os pontos da palavra do vocabulário.
    """
    # Soma dos pontos das letras
    soma = 0
    i = 0
    while i < len(palavra):
        letra = palavra[i]
        soma = soma + PONTUACAO_DAS_LETRAS[letra]
        i = i + 1
    return soma


def indice_na_ordem(letra):
    """
    Função auxiliar que devolve o índice da letra letra na constante LETRAS.
    """
    i = 0
    while i < len(LETRAS):
        if LETRAS[i] == letra:
            return i
        i = i + 1


def compara_palavras_por_ordem(p1, p2):
    """
    Função auxiliar que compara as duas palavras p1 e p2 segundo a ordem da constante LETRAS.
    Retorna:
    Devolve -1 se p1 vem antes de p2
    Devolve 0 se forem iguais
    Devolve 1 se p1 vem depois de p2
    """
    i = 0
    while i < len(p1) and i < len(p2):
        pos1 = indice_na_ordem(p1[i])
        pos2 = indice_na_ordem(p2[i])
        if pos1 < pos2:
            return -1
        if pos1 > pos2:
            return 1
        i = i + 1
    # se o ciclo acabou sem diferenças, significa que todas as letras até ao fim da mais curta são iguais
    # agora decide-se apenas com base no tamanho das palavra
    if len(p1) < len(p2): # se uma for parte da outra, a mais curta vem primeiro
        return -1
    if len(p1) > len(p2):
        return 1
    return 0 # têm todas as palavras iguais e o mesmo comprimento


def obtem_palavras(vocabulario, comp, letra):
    """
    Seletor:
    Cada par do tuplo contém a palavra e a respetiva pontuação. 
    Os pares estão ordenados por ordem decrescente de pontuação das palavras, e em caso
    de empate, em ordem lexicográfica. 
    Caso não existam no vocabulário palavras com o comprimento e primeira letra indicados, 
    a função deverá devolver um tuplo vazio
    Argumentos:
    vocabulario --> vocabulário
    comp --> int
    letra --> String
    Returns:
    Devolve um tuplo de pares que correspondem a todas as palavras com comprimento comp e primeira letra letra
    """
    # Verifica se existem palavras com esse comprimento e letra
    if comp not in vocabulario or letra not in vocabulario[comp]:
        return ()

    palavras = vocabulario[comp][letra]  # lista de strings
    # cria lista de pares já com a pontuação
    pares = []
    i = 0
    while i < len(palavras): # percorre todas as palavras da lista 'palavras'
        palavra_atual = palavras[i] # obtém a palavra atual
        acc_pontuacao_palavra = 0
        n = 0
        while n < len(palavra_atual): # percorre todas as letras da palavra 'w'
            acc_pontuacao_palavra = acc_pontuacao_palavra + PONTUACAO_DAS_LETRAS[palavra_atual[n]] # adiciona ao total a pontuação da letra atual
            n = n + 1
        pares.append((palavra_atual, acc_pontuacao_palavra)) # adiciona à lista um tuplo (palavra, soma de pontos)
        i = i + 1

    # As palavras com mais pontos vêm primeiro, ordem decrescente
    indice_atual = 1
    while indice_atual < len(pares):  # percorre a lista a partir do segundo elemento
        palavra_atual = pares[indice_atual][0]  # palavra atual
        pontos_atuais = pares[indice_atual][1]   # pontuação dessa palavra
        indice_de_comparacao = indice_atual - 1 # começa a comparar com o elemento anterior

        # Move os elementos enquanto:
        # o anterior tiver menos pontos, ou tiver a mesma pontuação mas vier depois na ordem LETRAS
        while indice_de_comparacao >= 0 and (pares[indice_de_comparacao][1] < pontos_atuais or (pares[indice_de_comparacao][1] == pontos_atuais and compara_palavras_por_ordem(pares[indice_de_comparacao][0], palavra_atual) > 0)):
            # Move o par anterior uma posição à frente
            pares[indice_de_comparacao + 1] = pares[indice_de_comparacao]
            # Continua a comparar com o elemento anterior (para trás)
            indice_de_comparacao = indice_de_comparacao - 1

        # Quando sair do ciclo, insere o par atual (palavra, pontos) na posição correta
        pares[indice_de_comparacao + 1] = (palavra_atual, pontos_atuais)

        # Passa ao próximo elemento da lista
        indice_atual = indice_atual + 1

    # converter para tuplo
    res = ()
    for i in range(len(pares)):
        res = res + (pares[i],)
    return res


def testa_palavra_padrao(vocabulario, palavra, padrao, letras):
    """
    Teste:
    Testa se é possível formar a palavra fornecida substituindo os carateres '.' do padrão por letras.
    Argumentos:
    vocabulario --> voicabulário
    palavra --> String
    padrao --> String
    letras --> String
    Returns:
    Devolve True caso exista a palavra no vocabulário e seja possível formar a
    palavra fornecida substituindo os carateres '.' do padrão por letras. 
    Caso contrário, devolve False
    """
    # Verifica se os tamanhos coincidem
    if len(palavra) != len(padrao):
        return False

    comprimento = len(palavra)
    letra_incial = palavra[0]
    if comprimento not in vocabulario or letra_incial not in vocabulario[comprimento]:
        return False

    # verificaa existência da palavra
    existe = False
    lista = vocabulario[comprimento][letra_incial]
    i = 0
    while i < len(lista):
        if lista[i] == palavra:
            existe = True
            break
        i = i + 1
    if not existe:
        return False

    # verifica as posições fixas do padrão
    i = 0
    while i < comprimento:
        if padrao[i] != '.' and padrao[i] != palavra[i]:
            return False
        i = i + 1

    # contar letras disponíveis do jogador
    conta = {} # cria um dicionário vazio onde se vai guardar o número de ocorrencias da letra
    i = 0
    while i < len(letras):
        caracter = letras[i]
        if caracter in conta: # se letra já existe
            conta[caracter] = conta[caracter] + 1 # soma um à contagem
        else:
            conta[caracter] = 1 # inicializa a contagem a um para avançar a seguir para a proxima posicao 
        i = i + 1

    # utilizar apenas as posições livres do padrão
    i = 0
    while i < comprimento:
        if padrao[i] == '.': # so é necessario letras nas posicoes livres
            letra = palavra[i] # letra atual do jogador
            if letra in conta: # vê quantas dessa letra ainda temos disponíveis
                q = conta[letra] # quantidade disponivel
            else:
                q = 0 # nao temos nehuma letra igual a essa
            if q == 0: # nao da para formar a palavra
                return False
            conta[letra] = q - 1 # utiliza se uma unidade dessa letra
        i = i + 1 # avanca para proxima posicao
    return True # é possivel formar a palavra


def ficheiro_para_vocabulario(nome_fich):
    """
    Transformador:
    Devolve o vocabulário formado a partir das palavras contidas no ficheiro. 
    O ficheiro contém uma palavra por linha, podendo ter linhas vazias, que são ignoradas.
    As palavras do ficheiro são sequências de carateres únicas de comprimento arbitrário, contendo potencialmente qualquer caracter. 
    Argumentos:
    nome_ficheiro --> String
    Returns:
    Devolve o vocabulário formado a partir das palavras contidas no ficheiro. 
    """
    if not isinstance(nome_fich, str) or nome_fich.strip() == '':
        raise ValueError('ficheiro_para_vocabulario: argumento inválido')
    letras_possiveis = {}
    i = 0
    while i < len(LETRAS):
        letras_possiveis[LETRAS[i]] = True
        i = i + 1 # Constrói um dicionário { letra: True } com todas as letras válidas
    validas = [] # Acumular palavras válidas, únicas, já em maiúsculas
    vistos = {} # Lista com as palavras já processadas
    with open(nome_fich, 'r', encoding='utf-8') as f: # vai ler cada linha, ignora espaços e linhas vazias
        for linha in f:
            palavra = linha.strip()
            if palavra == '':
                continue
            
            palavra_maiuscula = palavra.upper()
            n = len(palavra)

            # verifica tamanho
            if n < 2 or n > 15:
                continue

            # verifica letras
            i = 0
            controlo = True
            while i < n:
                if palavra_maiuscula[i] not in letras_possiveis:
                    controlo = False
                    break
                i = i + 1
            if not controlo:
                continue

            # verifica duplicados
            if palavra_maiuscula not in vistos:
                vistos[palavra_maiuscula] = True
                validas.append(palavra_maiuscula)

    # converte lista para tuplo uma única vez
    return cria_vocabulario(tuple(validas))


def vocabulario_para_str(vocabulario):
    """
    Transformador:
    Argumentos:
    vocabulario: vocabulário
    Returns:
    Devolve uma cadeia de caracteres que concatena todas as palavras guardadas no vocabulario, 
    separadas por um carácter de mudança de linha. 
    """
    texto = ''
    # percorre os comprimentos por ordem crescente
    comprimentos = sorted(vocabulario.keys()) # ordem crescente de comprimento
    for comprimento in comprimentos:
        # ordenar as iniciais segundo a ordem de LETRAS
        iniciais_ordenadas = sorted(vocabulario[comprimento].keys(), key=lambda x: LETRAS.index(x))

        # percorre as iniciais na ordem definida
        for ini in iniciais_ordenadas:
            # obtém todas as palavras do vocabulário que começam por essa letra e têm o comprimento atual
            # devolve uma lista de pares (palavra, pontuação)
            grupo = obtem_palavras(vocabulario, comprimento, ini)
            i = 0
            # percorre todas as palavras do grupo
            while i < len(grupo):
                palavra = grupo[i][0] # extrai apenas a palavra, ignorando a pontuação
                if texto == '': # se for a primeira palavra
                    texto = palavra
                else: # se não for a primeira palavra
                    texto = texto + '\n' + palavra
                i += 1
    return texto

"""Funções de alto nível associadas a TAD vocabulario"""
def procura_palavra_padrao(vocabulario, padrao, letras, min_pontos):
    """
    Procura no vocabulário a melhor palavra possível, com maior pontuação, que 
    se ajuste ao padrão fornecido e possa ser formada com as letras disponíveis.
    Argumentos:
    vocabulario: vocabulário
    padrao --> String
    padrao: padrão com letras fixas e pontos '.' para espaços livres
    letras --> String
    letras: letras disponíveis para preencher os pontos
    min_pontos --> int
    min_pontos: pontuação mínima aceitável
    Returns:
    Devolve o tuplo formado pela palavra e a pontuação, que correspondem à palavra do vocabulario
    com maior pontuação que é possível formar utilizando as letras da cadeia de carateres 
    para completar todos os espaços livres do padrão, cumprindo a restrição de que a pontuação da palavra 
    não pode ser inferior a min pontos.
    Caso a função não encontre nenhuma palavra, devolve o tuplo ('', 0).
    """
    # se o padrão estiver vazio então não há palavra possível
    if len(padrao) == 0:
        return ('', 0)
    
    melhor_palavra = '' # inicializa a palavra com maior pontuação
    melhor_pontos = 0 # inicializa a pontuação da palavra com maior pontuação

    # Determina as letras iniciais possíveis
    iniciais = []
    if padrao[0] == '.':
        # considera-se como iniciais todas as letras disponiveis do jogador em ordem lexicografica
        for c in sorted(letras): # põe na ordem lexicográfica
            if c not in iniciais:
                iniciais.append(c)
    else:
        iniciais = [padrao[0]]

    # Percorre todas as letras iniciais possíveis
    for ini in iniciais:
        # obtem todas as palavras do vocabulário com o mesmo comprimento e começadas pela letra inicial atual
        palavras = obtem_palavras(vocabulario, len(padrao), ini)
        for i in range(len(palavras)): # percorre todas as palavras desse grupo
            palavra = palavras[i][0] # extrai apenas a palavra do par (palavra, pontos)
            # verifica se a palavra se ajusta ao padrão e pode ser formada com as letras disponíveis
            if testa_palavra_padrao(vocabulario, palavra, padrao, letras):
                pontos = obtem_pontos(vocabulario, palavra) # calcula a pontuação total da palavra
                if pontos >= min_pontos: # respeita o minimo
                    if pontos > melhor_pontos or (pontos == melhor_pontos and (melhor_palavra == '' or compara_palavras_por_ordem(palavra, melhor_palavra) < 0)):
                        # se a palavra atual tiver mais pontos ou empatar mas vier antes na ordem lexicográfica, passa a ser a melhor
                        melhor_palavra = palavra
                        melhor_pontos = pontos

    return (melhor_palavra, melhor_pontos)


"""
TAD tabuleiro é usado para representar um tabuleiro do jogo Scrabble e as letras nele colocadas.
Operações básicas associadas a TAD tabuleiro
"""
def cria_tabuleiro():
    """
    Construtor:
    Cria um tabuleiro de Scrabble.
    Returns:
    Devolve um tabuleiro de Scrabble vazio.
    """
    tabuleiro = [['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']]
    return tabuleiro


def obtem_letra(t, c):
    """
    Seletor:
    Obtém o conteúdo de uma casa do tabuleiro.
    Argumentos:
    t: Tabuleiro.
    c: Casa
    Returns:
    Devolve a letra contida na casa c do tabuleiro t.
    """
    letra = t[c[0]-1][c[1]-1]
    return letra


def insere_letra(t, c, l):
    """
    Modificador:
    Escreve uma letra na casa especificada e retorna o tabuleiro.
    Argumentos:
    t: Tabuleiro.
    c: Casa (linha, coluna).
    l --> String
    l: Letra a inserir.
    Returns:
    tab --> Lista
    tab: O próprio tabuleiro após a inserção.
    """
    t[c[0]-1][c[1]-1] = l # Subtrai-se 1 a cada coordenada porque as casas são numeradas de 1 a 15,
    # mas os índices das listas em Python começam em 0.
    return t


def eh_tabuleiro(arg):
    """
    Reconhecedor:
    Devolve True caso o seu argumento seja um TAD tabuleiro e False caso contrário.
    Argumentos:
    arg --> Universal
    Returns:
    Devolve True caso o seu argumento seja um TAD tabuleiro e False caso contrário.
    """
    if not isinstance(arg, list):
        return False
    if len(arg) != TAMANHO_DO_TABULEIRO:
        return False
    for linha in arg:
        if not isinstance(linha, list) or len(linha) != TAMANHO_DO_TABULEIRO:
            return False
        for elem in linha:
            if not (elem == '.' or (isinstance(elem, str) and elem in LETRAS and len(elem) == 1)):
                return False
    return True


def eh_tabuleiro_vazio(arg):
    """
    Reconhecedor:
    Devolve True caso o seu argumento seja um TAD tabuleiro e estiver vazio (sem letras) e False caso contrário.
    Argumentos:
    arg
    Returns:
    Devolve True caso o seu argumento seja um TAD tabuleiro e estiver vazio (sem letras) e False caso contrário.
    """
    if not eh_tabuleiro(arg):
        return False
    for linha in arg:
        for elem in linha:
            if elem != '.':
                return False
    return True


def tabuleiros_iguais(t1, t2):
    """
    Teste:
    Testa se dois tabuleiros são iguais.
    Argumentos:
    t1 --> Universal
    t2 --> Universal
    Returns:
    Devolve True apenas se t1 e t2 forem tabuleiros e forem iguais.
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


def tabuleiro_para_str(t):
    """
    Transformador:
    Transforma o tabuleiro numa cadeia de caracteres que o representa.
    Argumentos:
    t: Tabuleiro.
    Returns:
    estrutura --> String
    estrutura: representacao externa do tabuleiro
    """
    primeira_linha = '                       1 1 1 1 1 1'
    segunda_linha = '     1 2 3 4 5 6 7 8 9 0 1 2 3 4 5'
    limites_horizontais = '   +-------------------------------+'
    estrutura = primeira_linha + '\n' + segunda_linha + '\n' + limites_horizontais + '\n'

    linha = 1
    while linha <= TAMANHO_DO_TABULEIRO:
        # formata o número da linha com um espaço à esquerda para alinhar
        if linha < 10:
            num = ' ' + str(linha)
        else:
            num = str(linha)

        corpo = ''
        coluna = 0
        while coluna < TAMANHO_DO_TABULEIRO:
            # adiciona o conteúdo da casa correspondente
            corpo = corpo + t[linha-1][coluna]
            # adiciona um espaço entre colunas, mas não no fim da linha
            if coluna < TAMANHO_DO_TABULEIRO -1:
                corpo = corpo + ' '
            coluna = coluna + 1

        estrutura = estrutura + num + ' | ' + corpo + ' |\n'
        linha = linha + 1
    
    estrutura = estrutura + limites_horizontais
    return estrutura

        
"""Funções de alto nível associadas a TAD tabuleiro"""
def obtem_padrao(t, i, f):
    """
    Devolve a sequência de letras contida no tabuleiro t entre a casa i e a casa f (ambas inclusive) na mesma linha vertical ou horizontal.
    Argumentos:
    t: Tabuleiro.
    i: casa inicial
    f: casa final
    Returns:
    Devolve a sequência de letras contida no tabuleiro t entre a casa i e a casa f (ambas inclusive) na mesma linha vertical ou horizontal.
    """
    linha_inicial = obtem_lin(i)
    coluna_inicial = obtem_col(i)
    linha_final = obtem_lin(f)
    coluna_final = obtem_col(f)

    # Caso horizontal
    if linha_inicial == linha_final:
        if coluna_inicial <= coluna_final: # define a ordem: esquerda para direita
            coluna_min = coluna_inicial
            coluna_max = coluna_final
        else:
            coluna_min = coluna_final # se vierem invertidas entao troca
            coluna_max = coluna_inicial

        res = ''
        while coluna_min <= coluna_max: # começa na coluna mínima e percorre até à coluna máxima (inclusive)
            res = res + obtem_letra(t, (linha_inicial, coluna_min))
            coluna_min = coluna_min + 1
        return res

    # Caso vertical (mesma coluna)
    if coluna_inicial == coluna_final:
        if linha_inicial <= linha_final: # define a ordem: cima para baixo
            linha_min = linha_inicial
            linha_max = linha_final
        else:
            linha_min = linha_final # se vierem invertidas entao troca
            linha_max = linha_inicial

        res = ''
        while linha_min <= linha_max: # começa na linha mínima e percorre até à linha máxima (inclusive)
            res = res + obtem_letra(t, (linha_min, coluna_inicial))
            linha_min = linha_min + 1
        return res


def insere_palavra(t, c, d, p):
    """
    Modifica destrutivamente o tabuleiro t colocando a palavra p na casa c na direção d.
    Argumentos:
    t: Tabuleiro.
    c: Casa inicial (linha, coluna).
    d --> String
    d: 'H' horizontal, 'V' vertical.
    p --> String
    p: Palavra a inserir.
    Returns: 
    t : Tabuleiro após a escrita.
    Devolve o próprio tabuleiro.
    """
    # linha e coluna de partida
    proxima_linha = c[0]
    proxima_coluna = c[1]

    # percorre todas as letras da palavra e insere uma a uma
    i = 0
    while i < len(p):
        # cria a casa atual com base nas coordenadas atuais
        casa_atual = cria_casa(proxima_linha, proxima_coluna)
        # insere a letra na casa atual do tabuleiro
        insere_letra(t, casa_atual, p[i])

        # atualiza as coordenadas para a próxima letra
        if d == 'H':
            # na horizontal, a linha mantém-se e a coluna avança
            proxima_coluna = proxima_coluna + 1
        else:
            # na vertical, a coluna mantém-se e a linha avança
            proxima_linha = proxima_linha + 1

        i = i + 1

    return t


def obtem_subpadroes(t, i, f, l):
    """
    Gera todos os subpadrões viáveis contidos entre duas casas do tabuleiro, na mesma linha ou coluna.
    Argumentos:
    t: Tabuleiro.
    i: Casa inicial (linha, coluna).
    f: Casa final
    l --> Inteiro
    l: Máximo de espaços livres.
    Returns:
    Devolve dois tuplos de igual tamanho.
    O primeiro tuplo contém todos os subpadrões viáveis ordenados gerados a partir do padrão original
    contido no tabuleiro t entre as casas i e f (ambas inclusive) com no máximo l espaços livres.
    Os sub-padrões inviáveis são os:
    1) que não contenham qualquer letra e sejam apenas constituídos por espaços livres,
    porque todas as jogadas válidas devem usar pelo menos uma letra do tabuleiro;
    (2) que não contenham qualquer espaço livre e sejam apenas constituídos por letras,
    porque todas as jogadas válidas devem usar pelo menos uma das letras do jogador;
    (3) para os quais exista no padrão original uma letra na posição anterior à da primeira
    posição do sub-padrão, ou exista no padrão original uma letra na posição
    seguinte à última posição do sub-padrão, para não sobrepor ou colar com palavras
    já existentes no tabuleiro.
    O segundo tuplo contém a casa onde
    começa cada um dos o subpadrões correspondentes do primeiro tuplo. 
    As casas i e f pertencem à mesma linha vertical ou horizontal.
    """
    linha_inicial = obtem_lin(i)
    coluna_inicial = obtem_col(i)
    linha_final = obtem_lin(f)
    coluna_final = obtem_col(f)

    # Verifica se é um padrão horizontal
    if linha_inicial == linha_final:
        if coluna_inicial <= coluna_final: # garante a leitura da esquerda para a direita
            coluna_min = coluna_inicial
            coluna_max = coluna_final
        else:
            coluna_min = coluna_final # se vierem invertidas entao troca
            coluna_max = coluna_inicial
        # Verifica se é um padrão horizontal
        direcao = 'H'
        padrao = obtem_padrao(t, cria_casa(linha_inicial, coluna_min), cria_casa(linha_inicial, coluna_max))
        linha_base = linha_inicial
        coluna_base = coluna_min
        tamanho_palavra = len(padrao)

    # Caso vertical (mesma coluna)
    elif coluna_inicial == coluna_final:
        if linha_inicial <= linha_final: # garante a leitura de cima para baixo
            linha_min = linha_inicial
            linha_max = linha_final
        else:
            linha_min = linha_final # se vierem invertidas entao troca
            linha_max = linha_inicial
        # Define direção e obtém o padrão
        direcao = 'V'
        padrao = obtem_padrao(t, cria_casa(linha_min, coluna_inicial), cria_casa(linha_max, coluna_inicial))
        linha_base = linha_min
        coluna_base = coluna_inicial
        tamanho_palavra = len(padrao)

    subpadroes = () # vai guardar os subpadrões viaveis
    casas = () # vai guardar as casas iniciais onde cada subpadrão começa
    # percorre todos os índices possíveis de início e fim de subpadrões
    for i in range(tamanho_palavra): # i: índice inicial do subpadrão
        for j in range(tamanho_palavra, i, -1): # j: índice final do subpadrão
            subpadrao_atual = padrao[i:j]
            # contar letras e pontos ('.')
            tem_letra = False
            tem_ponto = False
            pontos = 0
            for caracter in subpadrao_atual:
                if caracter == '.':
                    tem_ponto = True
                    pontos = pontos + 1
                else:
                    tem_letra = True
            # regras de viabilidade
            if not tem_letra or not tem_ponto:
                continue                  # precisa ter pelo menos 1 letra e 1 ponto
            if pontos > l:
                continue  # não pode exceder o máximo de espaços livres
            if i - 1 >= 0 and padrao[i - 1] != '.':
                continue                  # à esquerda não pode haver letra
            if j < tamanho_palavra and padrao[j] != '.':
                continue                  # à direita não pode haver letra

            # calcula a casa inicial correspondente ao subpadrao
            if direcao == 'H':
                inicio = cria_casa(linha_base, coluna_base + i)
            else:
                inicio = cria_casa(linha_base + i, coluna_base)
            # adiciona o subpadrão e a casa às respetivas listas
            subpadroes = subpadroes + (subpadrao_atual,)
            casas = casas + (inicio,)
    return subpadroes, casas


def gera_todos_padroes(t, l):
    """
    Percorre o tabuleiro completo e recolhe todos os subpadrões viáveis
    existentes em cada linha inteira e cada coluna inteira, respeitando o limite de espaços livres
    por subpadrão
    Argumentos:
    t: Tabuleiro.
    l --> int
    l: Máximo de espaços livres.
    Returns:
    Devolve três tuplos de igual tamanho.
    O primeiro contém todos os sub-padrões viáveis do tabuleiro que contenham no máximo l espaços
    livres, formado pelos sub-padrões ordenados obtidos de cada uma das linhas completas do tabuleiro 
    (da primeira à última), seguidos dos sub-padrões ordenados obtidos de cada coluna completa (da primeira até à última). 
    O segundo e terceiro tuplos, correspondem à casa de início 
    e à direção ('V' ou 'H') do sub-padrão correspondente do primeiro tuplo
    """
    padroes = ()
    casas_inicio = ()
    direcoes = ()

    # Linhas completas (H)
    for linha in range(1, TAMANHO_DO_TABULEIRO + 1):           
        casa_inicial = cria_casa(linha, 1)                     # casa inicial da linha (coluna 1)
        casa_final = cria_casa(linha, TAMANHO_DO_TABULEIRO)      # casa final da linha (última coluna)
        subpadroes, casas_de_inicio = obtem_subpadroes(t, casa_inicial, casa_final, l) # obtém subpadrões e as casas de início                                                                  
        for i in range(len(subpadroes)):                        # percorre os subpadrões encontrados
            padroes = padroes + (subpadroes[i],)                         # junta o subpadrão i
            casas_inicio = casas_inicio + (casas_de_inicio[i],)                # junta a casa de início correspondente
            direcoes = direcoes + ('H',)                                  # marca direção horizontal

    for coluna in range(1, TAMANHO_DO_TABULEIRO + 1):           
        casa_inicial = cria_casa(1, coluna)                                # casa inicial da coluna (linha 1)
        casa_final = cria_casa(TAMANHO_DO_TABULEIRO, coluna)             # casa final da coluna (última linha)
        subpadroes, casas_de_inicio = obtem_subpadroes(t, casa_inicial, casa_final, l)   # obtém subpadrões e as casas de início
        # acrescenta cada subpadrão encontrado nesta coluna às coleções finais
        for i in range(len(subpadroes)):                        # percorre os subpadrões encontrados
            padroes = padroes + (subpadroes[i],)                         # junta o subpadrão i
            casas_inicio = casas_inicio + (casas_de_inicio[i],)                       # junta a casa de início correspondente
            direcoes = direcoes + ('V',)                                  # marca direção vertical
    return padroes, casas_inicio, direcoes


def cria_conjunto(let, occ):
    """
    Cria um dicionário com as letras e o número de ocorrências de cada uma.
    Argumentos:
    let --> Tuplo com letras, cada uma única, pertencentes a LETRAS.
    occ --> Tuplo com o n.º de vezes que cada letra aparece.
    Returns:
    conj_letras --> Dicionário com cada letra e a respetiva quantidade.
    """
    if not isinstance(let, tuple) or not isinstance(occ, tuple) or len(let) != len(occ):
        raise ValueError('cria_conjunto: argumentos inválidos')
    
    conj_letras = {}
    tamanho = len(let)
    for i in LETRAS:
        contador = 0
        for j in let:
            if i == j:
                contador = contador + 1
        if contador > 1:
            raise ValueError('cria_conjunto: argumentos inválidos')

    for i in range(tamanho):
        if let[i] not in LETRAS or not isinstance(occ[i], int) or occ[i] <= 0 or occ[i] > 15:
            raise ValueError('cria_conjunto: argumentos inválidos')
        else:
            conj_letras[let[i]] = occ[i]

    return conj_letras


def gera_numero_aleatorio(estado): 
    """
    É responsável por produzir um novo número pseudo-aleatório a partir de um estado inicial.
    Argumentos:
    estado --> Inteiro.
    Returns:
    Valor pseudo-aleatório --> Inteiro
    """
    s = estado
    s ^= (s << 13) & 0xFFFFFFFF
    s ^= (s >> 17) & 0xFFFFFFFF
    s ^= (s << 5) & 0xFFFFFFFF
    return s


def permuta_letras(letras, estado):
    """
    Utiliza os números gerados por gera_numero_aleatorio para baralhar a lista de letras.
    Argumentos:
    letras --> Lista de letras a baralhar.
    estado --> Inteiro
    estado: Estado do gerador pseudo-aleatório.
    Returns:
    None
    """
    for i in range(len(letras) - 1, 0, -1):  
        estado = gera_numero_aleatorio(estado)
        j = estado % (i + 1)
        letras[i], letras[j] = letras[j], letras[i]
    return None


def baralha_conjunto(conj, estado):
    """
    Recebe um conjunto de letras e um inteiro positivo e devolve uma lista
    baralhada com todas as letras contidas no conjunto de letras. 
    Para baralhar as letras é construída uma lista com todas as letras contidas 
    no conjunto e depois permutam-se as letras.
    Argumentos:
    conj --> Dicionário
    conj: Conjunto de letras com quantidades.
    estado --> Inteiro
    estado: Estado para o processo de baralhar.
    Returns:
    lista_letras --> Lista
    lista_letras: Lista baralhada com todas as letras.
    """
    lista_letras = []
    for i in LETRAS:
        if i in conj:
            for j in range(conj[i]):
                lista_letras = lista_letras + [i]
    permuta_letras(lista_letras, estado)
    return lista_letras


def baralha_saco(seed): 
    """
    Baralha as letras contidas no saco.
    Argumentos:
    seed --> Int
    seed: Estado inicial do gerador pseudo-aleatório.
    Returns:
    Devolve uma lista baralhada com todas as letras contidas no saco de Scrabble.
    """
    if not isinstance(seed, int) or seed <= 0:
        raise ValueError('baralha_saco: argumento inválido')

    # Numero de ocorrências por letra 
    # A ordem é igual à da constante LETRAS
    letras = LETRAS
    ocorrencias = (14, 3, 4, 2, 5, 11, 2, 2, 2, 10, 2, 5, 6, 4, 10, 4, 1, 6, 8, 5, 7, 2, 1, 1)
    
    conj = cria_conjunto(letras, ocorrencias)
    saco = baralha_conjunto(conj, seed)
    return saco


def joga_palavra(tab, palavra, casa, direcao, conj_letras, primeira):
    """
    Tenta colocar uma palavra no tabuleiro segundo as regras.
    Argumentos:
    tab --> Lista
    tab: Tabuleiro.
    palavra --> String
    palavra: Palavra a jogar.
    casa --> Tuplo
    casa: Casa inicial (linha, coluna).
    direcao --> String
    direcao: 'H' ou 'V'.
    conj_letras --> Dicionário
    conj_letras: Letras disponíveis do jogador.
    primeira --> Booleano
    primeira: True se for a primeira jogada.
    Returns:
    Tuplo com as letras gastas ou tuplo vazio () se a jogada for inválida.
    """
    if direcao == 'H':
        if len(palavra) + casa[1] - 1 > TAMANHO_DO_TABULEIRO:   # verifica se cabe na horizontal
            return ()
    else:
        if casa[0] - 1 + len(palavra) > TAMANHO_DO_TABULEIRO:   # verifica se cabe na vertical
            return ()
    
    utilizadas = {} # dicionario com as letras novas que o jogador tera de gastar
    controlo = False    # sinaliza se a palavra partilha pelo menos uma letra já presente no tabuleiro. Obrigatorio a partir da segunda jogada
    # Percorre cada letra da palavra e valida sobreposição e uso de letras do jogador
    j = 0
    while j < len(palavra):
            caracter = palavra[j]
            if direcao == 'H':
                valor = tab[casa[0] - 1][casa[1] - 1 + j]
            else:
                valor = tab[casa[0] - 1 + j][casa[1] - 1]

            if valor == '.': # casa vazia logo vai usar letra do jogador
                if caracter in utilizadas:
                    utilizadas[caracter] = utilizadas[caracter] + 1
                else:
                    utilizadas[caracter] = 1
            else:
                if valor != caracter: # casa ja ocupada logo tem de coincidir com a letra jogada
                    return ()
                controlo = True # marca que a nova palavra toca numa palavra existente
            j = j + 1   
    # Regras para a primeira jogada
    if primeira == True:
            if len(palavra) < 2: # A primeira palavra tem de ter pelo menos 2 letras
                return ()
            if direcao == 'H':
                # Tem de estar na linha 8 e cobrir a coluna 8
                if not (casa[0] == 8 and casa[1] <= 8 <= casa[1] + len(palavra) - 1):
                    return ()
            else:
                # Tem de estar na coluna 8 e cobrir a linha 8
                if not (casa[1] == 8 and casa[0] <= 8 <= casa[0] + len(palavra) - 1):
                    return ()
               
    else:
        # A partir da segunda jogada, a palavra tem de tocar em algo já no tabuleiro
        if not controlo: # nas jogadas seguintes as palavras devem se continuar a ligar
            return ()

    # Verificar se o jogador tem as letras necessárias para preencher as casas vazias
    k = 0
    letras_utilizadas = list(utilizadas.keys())
    while k < len(letras_utilizadas):
            if letras_utilizadas[k] not in conj_letras or utilizadas[letras_utilizadas[k]] > conj_letras[letras_utilizadas[k]]:
                return ()
            k = k + 1

    insere_palavra(tab, casa, direcao, palavra) # escreve palavra no tabuleiro
    # Constroi o tuplo das letras utilizadas 
    res = ()
    for n in range(len(LETRAS)):
        if LETRAS[n] in utilizadas:
            p = 0
            while p < utilizadas[LETRAS[n]]:
                res = res + (LETRAS[n],)
                p = p + 1
    return res


def pontuacao_palavra(palavra):
    """
    Devolve a pontuação da palavra.
    """
    total = 0
    i = 0
    while i < len(palavra):
        total = total + PONTUACAO_DAS_LETRAS[palavra[i]]
        i = i + 1
    return total


def jogada_humano(tab, jog, vocab, pilha):
    """
    A função processa o turno completo do jogador humano
    Formato válido:
    1) Passar: 'P'. A função devolve False sem alterar nenhum dos argumentos.
    2) Trocar: 'T <seq_letras>', sendo <seq_letras> a sequência de uma ou mais
    letras separada por espaços do conjunto de letras do jogador para trocar. 
    Caso a jogada seja válida, a função devolve True, modifica o jogador retirando novas
    letras do final da lista de letras (que é também modificada).
    3) Jogar: 'J <linha> <coluna> <dir> <palavra>'. Caso a jogada seja válida,
    a função devolve True e modifica o tabuleiro, atualiza o jogador, atualizando a
    sua pontuação e retirando novas letras do final da lista de letras (que é também
    modificada). 
    No caso da primeira jogada da partida (o tabuleiro não contém
    nenhuma palavra), a palavra colocada deve cobrir a casa central do tabuleiro.
    Para as jogadas seguintes serem válidas, as casas do tabuleiro onde se colocarem
    as palavras devem ser um padrão viável, e as palavras devem estar no vocabulario.
    Argumentos:
    tab: Tabuleiro
    jog: Jogador
    vocab: Vocabulário
    pilha --> lista
    pilha: lista de letras
    """
    if eh_humano(jog): # se for mesmo humano, obtém o nome
        nome = jogador_identidade(jog)

    # ciclo while acontece até executar uma jogada válida ou passar
    while True:
        comando = input(f'Jogada {nome}: ').strip() # lê linha e remove espaços iniciais e finais
        if comando == '': # comando vazio, entao volta a pedir
            continue
        partes = comando.split()  # separa por espaços

        # PASSAR
        if partes[0] == 'P' and len(partes) == 1:
            return False # não jogou (passou)

        # TROCAR
        if partes[0] == 'T' and len(partes) >= 2:
            sequencia = partes[1:] # letras a trocar
            # valida letras pedidas, têm de pertencer a LETRAS, e conta quantidades
            pedidas = {} # dicionário: letra --> quantas quer trocar
            valido = True
            for caracter in sequencia:
                if caracter not in LETRAS:
                    valido = False
                    break
                pedidas[caracter] = pedidas.get(caracter, 0) + 1
            if not valido:
                continue # volta a pedir comando

            # conta as letras que o jogador tem
            tem = {}
            i = 0
            while i < len(jog['letras']):
                caracter = jog['letras'][i]
                tem[caracter] = tem.get(caracter, 0) + 1
                i = i + 1

            # verifica se o jogador tem, para cada letra, pelo menos o numero pedido
            for letra in pedidas:
                quantidade_pedida = pedidas[letra]
                if tem.get(letra, 0) < quantidade_pedida:
                    valido = False
                    break
            if not valido:
                continue # volta a pedir comando
            # o saco tem de ter pelo menos tantas letras quanto as pedidas
            if len(pilha) < len(sequencia):
                continue
            # retira as letras pedidas ao jogador
            for caracter in sequencia:
                usa_letra(jog, caracter)
            # dá ao jogador o mesmo numero de letras do saco (do fim)
            for i in range(len(sequencia)):
                recebe_letra(jog, pilha.pop()) 
            return True

        # JOGAR PALAVRA
        if partes[0] == 'J' and len(partes) == 5:
            lin = int(partes[1]) # linha inicial
            col = int(partes[2]) # coluna inicial
            direcao = partes[3] # 'H' ou 'V'
            palavra = partes[4] # palavra a jogar
            if direcao != 'H' and direcao != 'V':
                continue
            # valida letras pedidas, têm de pertencer a LETRAS
            i = 0
            letras_validas = True
            while i < len(palavra):
                if palavra[i] not in LETRAS:
                    letras_validas = False
                    break
                i = i + 1
            if not letras_validas:
                continue
            
            # verifica se a palavra existe no vocabulário
            if obtem_pontos(vocab, palavra) == 0:
                continue

            # constroi o conjunto de letras do jogador e conta (letra --> quantidade)
            conj_letras = {}
            for caracter in jog['letras']:
                conj_letras[caracter] = conj_letras.get(caracter, 0) + 1

            # testa se é a primeira jogada: tabuleiro totalmente vazio
            primeira = eh_tabuleiro_vazio(tab)

            # tenta colocar a palavra no tabuleiro segundo as regras
            letras_gastas = joga_palavra(tab, palavra, cria_casa(lin, col), direcao, conj_letras, primeira)
            if letras_gastas == ():
                # inválida, pedir novo comando
                continue
            # pontuação simples da palavra
            soma_pontos(jog, pontuacao_palavra(palavra))

            # retirar do jogador apenas as letras gastas
            for caracter in letras_gastas:
                usa_letra(jog, caracter)

            # repor do saco o mesmo numero de letras
            for i in range(len(letras_gastas)):
                if len(pilha) == 0:
                    break
                recebe_letra(jog, pilha.pop())
            return True # jogada concluída
        # se não for P/T/J no formato certo, volta a pedir
        continue


def aplicar_jogada(tabuleiro, jogador, pilha, palavra, casa_inicial, direcao):
    """
    Executa uma jogada válida no tabuleiro.
    """
    # Extrai linha e coluna da casa inicial
    linha = obtem_lin(casa_inicial)
    coluna = obtem_col(casa_inicial)
    usadas = [] # guarda as letras colocadas no tabuleiro
    # Percorre cada letra da palavra
    i = 0
    while i < len(palavra):
        # Obtém a letra atual no tabuleiro (pode ser '.' ou uma letra fixa)
        if direcao == 'H':
            caracter_do_tab = obtem_letra(tabuleiro, (linha, coluna + i))  
        else:
            caracter_do_tab = obtem_letra(tabuleiro, (linha + i, coluna))
        # Se a casa estiver vazia, insere a nova letra e regista-a como usada
        if caracter_do_tab == '.':
            if direcao == 'H': 
                insere_letra(tabuleiro, (linha, coluna + i), palavra[i])
            else:              
                insere_letra(tabuleiro, (linha + i, coluna), palavra[i])
            usadas.append(palavra[i])
        i = i + 1
    soma_pontos(jogador, pontuacao_palavra(palavra))
    # Retira do jogador as letras que foram colocadas no tabuleiro
    j = 0
    while j < len(usadas): 
        usa_letra(jogador, usadas[j])
        j = j + 1
    # Recolhe do fim da pilha o mesmo número de letras usadas se houver
    k = 0
    while k < len(usadas) and len(pilha) > 0: 
        recebe_letra(jogador, pilha.pop())
        k = k + 1
    return True # Jogada concluída com sucesso


def jogada_agente(tabuleiro, jogador, vocabulario, pilha):
    """
    Decide e executa a jogada do agente.
    Ações possíveis:
    PASSAR: se for a primeira jogada (tabuleiro vazio) 
            ou se não conseguir nem jogar nem trocar.
    TROCAR: se não conseguir jogar e existirem pelo menos 7 letras no saco
            troca todas as letras do jogador por novas.
    JOGAR: se conseguir formar uma palavra válida com o vocabulário e as letras do jogador.
    Returns:
    Retorna True se jogar (J ou T) ou False se passar (P).
    """
    nivel = jogador.get('nivel', 'MEDIO') # obtém o nível do agente ('FACIL', 'MEDIO' ou 'DIFICIL') e usa 'FACIL' por defeito se não existir
    # Primeira jogada: o agente PASSA obrigatoriamente
    if eh_tabuleiro_vazio(tabuleiro):
        print('Jogada ' + nivel + ': P')
        return False

    # Obter letras e padrões
    letras_disponiveis = jogador_letras(jogador)     # letras do jogador como string
    num_letras = len(letras_disponiveis)

    # gerar todos os padrões possíveis
    padroes, casas, direcoes = gera_todos_padroes(tabuleiro, num_letras)

    # definir o passo de amostragem consoante o nível
    if nivel == 'FACIL':
        passo = 100
    elif nivel == 'MEDIO':
        passo = 50
    else:
        passo = 10  # DIFICIL

    # Selecionar 1 em cada N padrões com slicing [::N]
    parte_padroes_originais = padroes[::passo]
    casas_f = casas[::passo] # posições iniciais correspondentes aos padrões filtrados
    direcoes_f = direcoes[::passo] # direções (H ou V) correspondentes aos padrões filtrados

    # Procurar melhor palavra dentro dos padrões amostrados
    melhor_palavra = '' # inicializa a melhor palavra encontrada, nenhuma ainda
    melhor_pontos = -1 # pontuação máxima encontrada até agora
    melhor_indice = -1 #  guarda o índice do padrão vencedor dentro de parte_padroes_originais

    for i in range(len(parte_padroes_originais)):
        padrao = parte_padroes_originais[i] # obtém o padrão atual
        palavra, pontos = procura_palavra_padrao(vocabulario, padrao, letras_disponiveis, 0)  # tenta achar a melhor palavra para este padrão
        # guarda a palavra de maior pontuação
        if palavra != '' and pontos > melhor_pontos: # se encontrou palavra e supera a melhor pontuação
            melhor_palavra = palavra # atualiza a melhor palavra
            melhor_pontos = pontos # atualiza a melhor pontuação
            melhor_indice = i # número do padrão onde a melhor palavra foi encontrada

    # Se encontrou jogada válida, então joga
    if melhor_indice != -1: # se algum padrão deu uma jogada válida
        casa_escolhida = casas_f[melhor_indice] # casa inicial correspondente ao mesmo índice
        direcao_escolhida = direcoes_f[melhor_indice] # direção correspondente (H ou V)
        lin = obtem_lin(casa_escolhida)
        col = obtem_col(casa_escolhida)

        print(f'Jogada {nivel}: J {lin} {col} {direcao_escolhida} {melhor_palavra}') # imprime ação do agente
        # escreve no tabuleiro, soma pontos e repõe letras
        return aplicar_jogada(tabuleiro, jogador, pilha, melhor_palavra, casa_escolhida, direcao_escolhida)

    # Se não conseguiu jogar entao tenta TROCAR se apenas se houver mais de 7 letras no saco
    if len(pilha) >= 7 and num_letras > 0:
        letras_str = ' '.join(letras_disponiveis)  # formata para imprimir com espacos
        print(f'Jogada {nivel}: T {letras_str}')  # imprime ação de troca
        # retira todas as letras do jogador
        for letra in letras_disponiveis:
            usa_letra(jogador, letra)
        # repõe o mesmo número de letras a partir do fim da pilha
        for i in range(num_letras):  # volta a dar o mesmo nº de letras
            if len(pilha) == 0: # se o saco ficar vazio então pára
                break
            recebe_letra(jogador, pilha.pop()) # é retirada uma letra do fim da pilha para o jogador
        return True # a açao de troca foi executada
    # Caso contrário passa
    print('Jogada ' + nivel + ': P')
    return False # passou

def scrabble2(jogadores, nome_fich, seed):
    """
    Função principal que permite jogar um jogo completo de Scrabble2 de dois a quatro jogadores.
    O jogo começa baralhando o saco de letras e distribuindo o conjunto de 7 
    letras a cada um dos jogadores em ordem. 
    O jogo termina quando todos os jogadores passam ou quando um jogador fica sem letras
    e o saco estiver esgotado.
    Argumentos:
    jogadores --> Tuplo
    jogadores: Nome dos jogadores e o nível dos jogadores agentes na ordem em que jogam
    nome_fich --> String
    nome_fich: Nome do ficheiro com o vocabulário
    seed --> Inteiro
    seed: Estado inicial do gerador pseudo-aleatório
    Returns:
    Devolve o tuplo com a pontuação final obtida pelos jogadores
    """
    if not isinstance(jogadores, tuple) or len(jogadores) < 2 or len(jogadores) > 4:
        raise ValueError('scrabble2: argumentos inválidos')
    if not isinstance(nome_fich, str) or nome_fich.strip() == '':
        raise ValueError('scrabble2: argumentos inválidos')
    if not isinstance(seed, int) or seed < 0:
        raise ValueError('scrabble2: argumentos inválidos')

    indice = 0
    while indice < len(jogadores):
        valor = jogadores[indice]
        if not isinstance(valor, str) or valor.strip() == '':
            raise ValueError('scrabble2: argumentos inválidos')
        if valor[0] == '@':
            nivel = valor[1:]
            if nivel not in ('FACIL', 'MEDIO', 'DIFICIL'):
                raise ValueError('scrabble2: argumentos inválidos')
        indice = indice + 1

    # Preparação do jogo
    vocabulario = ficheiro_para_vocabulario(nome_fich)
    tabuleiro = cria_tabuleiro()
    saco = baralha_saco(seed)  # lista baralhada com todas as letras do saco

    # cria jogadores na ordem dada
    lista_jogadores = []
    i = 0
    while i < len(jogadores):  # percorre a descrição de cada jogador
        descricao = jogadores[i]
        if descricao[0] == '@':
            jogador = cria_agente(descricao[1:])
        else:
            jogador = cria_humano(descricao)
        lista_jogadores.append(jogador)
        i = i + 1
    # distribui 7 letras a cada jogador
    i = 0
    while i < len(lista_jogadores):
        distribui_letras(lista_jogadores[i], saco, 7)
        i = i + 1
    # apresentação inicial
    print('Bem-vindo ao SCRABBLE2.')
    print(tabuleiro_para_str(tabuleiro))
    i = 0
    while i < len(lista_jogadores):
        print(jogador_para_str(lista_jogadores[i]))
        i = i + 1
    # ciclo principal
    todos_passaram_seguidos = 0
    terminou = False

    while not terminou: # faz rondas completas enquanto o jogo nao terminar
        indice = 0
        while indice < len(lista_jogadores):  # percorre os jogadores por ordem de jogo
            jogador = lista_jogadores[indice] # jogador da vez
            # executar a jogada do humano ou do agente
            if eh_humano(jogador):
                jogou = jogada_humano(tabuleiro, jogador, vocabulario, saco)
            else:
                jogou = jogada_agente(tabuleiro, jogador, vocabulario, saco)
            if jogou: # true se jogou ou false se passou
                todos_passaram_seguidos = 0 # se alguem jogou o contador de passes seguidos volta ao inicio
            else:
                todos_passaram_seguidos = todos_passaram_seguidos + 1 # conta passes
  
            # condições de paragem:
            # 1: todos passaram consecutivamente
            # 2: alguém ficou sem letras e o saco está vazio
            sem_letras = len(jogador['letras']) == 0 # booleano controla se o jogador atual ficou sem letras
            saco_vazio = len(saco) == 0 # controla se o saco está vazio
            if todos_passaram_seguidos == len(lista_jogadores) or (sem_letras and saco_vazio):
                terminou = True # fim de jogo
            # mostrar tabuleiro e estado dos jogadores apenas se o jogo não terminou
            if not terminou:
                print(tabuleiro_para_str(tabuleiro))  # mostra tabuleiro após a jogada
                j = 0
                while j < len(lista_jogadores): # mostra o estado de cada jogador
                    print(jogador_para_str(lista_jogadores[j]))
                    j = j + 1
            else:
                break  # não imprime nada após a última jogada
            indice = indice + 1
    # Resultados
    resultados = ()
    i = 0
    while i < len(lista_jogadores):
        resultados = resultados + (jogador_pontos(lista_jogadores[i]),)
        i = i + 1
    return resultados