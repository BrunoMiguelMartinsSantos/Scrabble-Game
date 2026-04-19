# Fundamentos da Programação - 1.º Projeto
# Projeto: Jogo Scrabble
# Sou o Bruno Santos (ist1118057), aluno do 1.º ano da Licenciatura Bolonha em Engenharia Informática e de Computadores - Alameda.
# Email Pessoal: bruno793santos@gmail.com
# Email Institucional: bruno.martins.santos@tecnico.ulisboa.pt

LETRAS = ('A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O','P','Q','R','S','T','U','V','X','Z')
TAMANHO_DO_TABULEIRO = 15


def cria_conjunto(let, occ):
    """
    Cria um dicionário com as letras e o número de ocorrências de cada uma.
    Argumentos:
    let --> Tuplo com letras, cada uma única, pertencentes a LETRAS.
    occ --> Tuplo com o n.º de vezes que cada letra aparece.
    Returns:
    dict --> Dicionário com cada letra e a respetiva quantidade.
    """
    if not isinstance(let, tuple) or not isinstance(occ, tuple) or len(let) != len(occ):
        raise ValueError("cria_conjunto: argumentos inválidos")
    
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
            raise ValueError("cria_conjunto: argumentos inválidos")
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
    baralhada com todas as letras contidas no conjunto de letras. Para baralhar as letras é
    construída uma lista com todas as letras contidas no conjunto e depois permutam-se as letras.
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


def testa_palavra_padrao(palavra, padrao, conj):  
    """
    Verifica se uma palavra se pode encaixar num padrão usando apenas as letras disponíveis em conj.
    Argumentos:
    palavra --> String
    palavra: Palavra a colocar.
    padrao --> String
    padrao: Padrão com letras fixas e '.'.
    conj --> Dicionário
    conj: Letras disponíveis (letra --> quantidade).
    Returns:
    Booleano: True se a palavra respeita o padrão e os limites de conj, caso contrário False.
    """
    if len(palavra) != len(padrao):
        return False

    novo_conj = {}
    i = 0 
    tamanho = len(palavra) 

    while i < tamanho:
        if padrao[i] != '.':
            if padrao[i] != palavra[i]:
                return False
        else:
            if palavra[i] in novo_conj:  
                novo_conj[palavra[i]] = novo_conj[palavra[i]] + 1 
            else:
                novo_conj[palavra[i]] = 1 
        i = i + 1

    for j in novo_conj:
        if j not in conj or novo_conj[j] > conj[j]:
            return False
        
    return True


def cria_tabuleiro():
    """
    Cria e devolve uma matriz de listas.
    Returns:
    tabuleiro --> Lista
    tabuleiro: Lista de listas representando o tabuleiro.
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

 
def cria_casa(l, c):
    """
    Verifica uma posição (linha, coluna) no tabuleiro e devolve o tuplo (l, c)
    Argumentos:
    l --> Inteiro
    c --> Inteiro
    l : Linha.
    c : Coluna.
    Returns:
    Retorna o Tuplo (l, c) que corresponde à casa do tabuleiro.
    """
    if not isinstance(l, int) or not isinstance(c, int) or l > TAMANHO_DO_TABULEIRO or c > TAMANHO_DO_TABULEIRO or c <= 0 or l <= 0:
        raise ValueError('cria_casa: argumentos inválidos')
    return (l, c)


def obtem_valor(tab, casa): 
    """
    Obtém o conteúdo de uma casa do tabuleiro.
    Argumentos:
    tab --> Lista
    tab: Tabuleiro.
    casa --> Tuplo
    casa: Posição (linha, coluna).
    Returns:
    Valor --> String
    Valor : Letra na casa ou '.' se vazia.
    """
    valor = tab[casa[0]-1][casa[1]-1]
    return valor

 
def insere_letra(tab, casa, letra):
    """
    Escreve uma letra na casa especificada e retorna o tabuleiro.
    Argumentos:
    tab --> Lista
    tab: Tabuleiro.
    casa --> Tuplo
    casa: Posição (linha, coluna).
    Letra --> String
    letra: Letra a inserir.
    Returns:
    tab --> Lista
    tab: O próprio tabuleiro após a inserção.
    """
    tab[casa[0]-1][casa[1]-1] = letra # Subtrai-se 1 a cada coordenada porque as casas são numeradas de 1 a 15,
    # mas os índices das listas em Python começam em 0.
    return tab


def obtem_sequencia(tab, casa, direcao, tamanho):
    """
    Retorna uma string com comprimento especificado em tamanho formada pelas casas consecutivas, 
    na direção 'H' (horizontal) ou 'V' (vertical)
    Argumentos:
    tab --> Lista
    tab: Tabuleiro.
    casa --> Tuplo
    casa: Casa inicial (linha, coluna).
    direcao --> String
    direcao: 'H' para horizontal, 'V' para vertical.
    tamanho --> Inteiro
    tamanho: Comprimento da sequência.
    Returns:
    seq_caracteres --> String
    """
    seq_caracteres = ''

    if direcao == 'H':
        for i in range(tamanho):
            seq_caracteres = seq_caracteres + obtem_valor(tab, (casa[0], i + casa[1]))
    elif direcao == "V":
        for j in range(tamanho):
            seq_caracteres = seq_caracteres + obtem_valor(tab, (j + casa[0],casa[1]))
    else:
        raise ValueError("obtem_sequencia: argumentos inválidos")
    
    return seq_caracteres


def insere_palavra(tab, casa, direcao, palavra):
    """
    Escreve a palavra no tabuleiro a partir de casa, na direção 'H' ou 'V'. Retorna o tabuleiro modificado
    Argumentos:
    tab --> Lista
    tab: Tabuleiro.
    casa --> Tuplo
    casa: Casa inicial (linha, coluna).
    direcao --> String
    direcao: 'H' horizontal, 'V' vertical.
    palavra --> String
    palavra: Palavra a inserir.
    Returns:
    tab --> Lista   
    tab : Tabuleiro após a escrita.
    """
    if direcao == 'H':
        for i in range(len(palavra)):
            tab[casa[0]-1][i + casa[1]-1] = palavra[i]
    if direcao == "V":
        for j in range(len(palavra)):
            tab[j + casa[0]-1][casa[1]-1] = palavra[j]
    return tab


def tabuleiro_para_str(tab):
    """
    Transforma o tabuleiro numa cadeia de caracteres que o representa.
    Argumentos:
    tab --> Lista
    tab: Tabuleiro.
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
        if linha < 10:
            num = ' ' + str(linha)
        else:
            num = str(linha)

        corpo = ''
        coluna = 0
        while coluna < TAMANHO_DO_TABULEIRO:
            corpo = corpo + tab[linha-1][coluna]
            if coluna < TAMANHO_DO_TABULEIRO -1:
                corpo = corpo + ' '
            coluna = coluna + 1

        estrutura = estrutura + num + ' | ' + corpo + ' |\n'
        linha = linha + 1
    
    estrutura = estrutura + limites_horizontais
    return estrutura


def cria_jogador(ordem, pontos, conj_letras):
    """
    Cria um dicionário e efetua validacoes
    Argumentos:
    ordem --> Inteiro
    ordem: Ordem do jogador.
    pontos --> Inteiro
    pontos: Pontuação inicial.
    conj_letras --> Dicionário
    conj_letras: Letras do jogador.
    Returns:
    res --> Dicionário
    res: Informacoes do jogador: 'id', 'pontos' e 'letras'.
    """
    if not isinstance(ordem, int) or not isinstance(pontos, int) or not isinstance(conj_letras, dict) or ordem < 0 or ordem > 4 or pontos < 0:
        raise ValueError('cria_jogador: argumentos inválidos')
    
    soma = 0
    for l in conj_letras:
        if l not in LETRAS:
            raise ValueError('cria_jogador: argumentos inválidos')
        if not isinstance(conj_letras[l], int) or conj_letras[l] <= 0:
            raise ValueError('cria_jogador: argumentos inválidos')
        soma = soma + conj_letras[l]

    if soma > 7:
        raise ValueError('cria_jogador: argumentos inválidos')

    res = {}
    res['id'] = ordem
    res['pontos'] = pontos
    res['letras'] = conj_letras

    return res


def jogador_para_str(jog): 
    """
    Transforma o jogador numa cadeia de caracteres que o representa.
    Argumentos:
    jog --> Dicionário
    jog: Informacoes do jogador (id, pontos, letras).
    Returns:
    Retorna string do tipo "#<id> (<pontos>): <letras separadas por espaço>".
    """
    seq_letras = []
    i = 0
    while i < len(LETRAS):
        if LETRAS[i] in jog['letras']:
            k = 0
            while k < (jog['letras'][LETRAS[i]]):
                seq_letras = seq_letras + [LETRAS[i]]
                k = k + 1
        i = i + 1

    seq_letras_str = ''

    j = 0
    while j < len(seq_letras):
        seq_letras_str = seq_letras_str + seq_letras[j]
        if j != len(seq_letras) - 1:
            seq_letras_str = seq_letras_str + ' '
        j = j + 1

    pontos = str(jog['pontos'])

    if len(pontos) == 1:
        pontos = '  ' + pontos
    if len(pontos) == 2:
        pontos = ' ' + pontos

    return '#' + str(jog['id']) + ' (' + pontos + '): ' + seq_letras_str


def distribui_letra(letras, jogador): 
    """
    Tira uma letra do fim da lista letras e adiciona ao conjunto de letras do jogador
    Argumentos:
    letras --> Lista
    letras: Lista de letras.
    jogador --> Dicionário
    jogador: Informacoes do jogador modificadas.
    Returns:
    Booleano: True se distribuiu uma letra ou False se a lista estava vazia.
    """
    if letras != []:
        letra_removida = letras.pop(-1)
        if letra_removida in jogador['letras']: # Se o jogador ja tiver essa letra, soma-se 1 ao contador
            jogador['letras'][letra_removida] = jogador['letras'][letra_removida] + 1
        else: # Cria a nova entrada no dicionario com quantidade 1
            jogador['letras'][letra_removida] = 1
        return True # Indica se a distribuicao foi feita com sucesso
    else: 
        return False # Se a lista estiver vazia, nao ha letras para distribuir


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
    Tuplo com as letras gastas,
    ou tuplo vazio () se a jogada for inválida.
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

    # Construi o tuplo das letras utilizadas 
    res = ()

    for n in range(len(LETRAS)):
        if LETRAS[n] in utilizadas:
            p = 0
            while p < utilizadas[LETRAS[n]]:
                res = res + (LETRAS[n],)
                p = p + 1
    return res

def retira_letra(conj, letra):
    """
    Se letra existir, diminui 1 e remove a chave do dicionário quando chega a 0
    Argumentos:
    conj --> Dicionário
    conj: Conjunto do jogador (modificado).
    letra: Letra a retirar.
    letra --> String
    """
    if letra in conj:
        conj[letra] = conj[letra] - 1
        if conj[letra] == 0:
            del conj[letra]


def processa_jogada(tab, jog, pilha, pontos, primeira):
    """
    A funcao processa o turno completo do jogador
    Lê e processa um comando de jogada ('P', 'T', 'J'') para um jogador.
    Argumentos:
    tab --> Lista
    tab: Tabuleiro.
    jog --> Dicionário
    jog: Informacoes do jogador atual (modificada em caso de troca ou jogada).
    pilha --> Lista
    pilha: Lista de letras.
    pontos --> Dicionário 
    pontos: Pontos por letra.
    primeira --> Booleano
    primeira: True se for a primeira jogada da partida.
    Returns:
    Booleano: True se realizou uma acaoo (troca ou jogada), False se passou.
    """
    while True:  
        comando = input(f"Jogada J{jog['id']}: ") # Pede ao jogador que introduza um comando
        acao = comando.split() # divide o comando em partes separadas por espaços (lista de strings)

        if len(acao) == 0:  # se estiver vazio, pede de novo
            continue

        if acao[0] == 'P': # Passar
            return False

        if acao[0] == 'T':  # Trocar letras
            letras = acao[1:] # letras a trocar vem apos o 'T
            cont = {} # Conta quantas vezes cada letra foi pedida para troca
            for c in letras:
                cont[c] = cont.get(c, 0) + 1

            invalido = False
            for c in cont: # verifica se o jogador tem as letras pedidas
                if c not in jog['letras'] or jog['letras'][c] < cont[c]:
                    invalido = True
                    break
            
            # Se não tiver as letras suficientes, o comando inválido e pede outro
            if invalido == True:
                continue
            
            if len(pilha) < len(letras) or len(pilha) < 7: # verifica se o saco tem letras suficientes para efetuar a troca
                continue
            
            # Retira as letras indicadas do jogador
            for c in letras:
                retira_letra(jog['letras'], c)

            # Repõe a mesma quantidade de letras da pilha para o jogador
            for n in letras:
                if len(pilha) > 0:
                    distribui_letra(pilha, jog) # repõe do saco
            return True # Jogada realizada com sucesso

        # Jogar palavra
        if acao[0] == 'J':
            # Converte os argumentos de posição para inteiros
            linha = eval(acao[1])
            coluna = eval(acao[2])
            if type(linha) != int or type(coluna) != int:
                continue
            direcao = acao[3] # 'H' ou 'V'
            palavra = acao[4] # Palavra a jogar
            if direcao not in ('H', 'V'):
                continue
            # Verifica se a posição inicial está dentro do tabuleiro
            if not (1 <= linha <= TAMANHO_DO_TABULEIRO and 1 <= coluna <= TAMANHO_DO_TABULEIRO): # dentro do tabuleiro
                continue
            
            # Tenta jogar a palavra no tabuleiro, devolvendo as letras usadas
            utilizadas = joga_palavra(tab, palavra, cria_casa(linha, coluna), direcao, jog['letras'], primeira)
            if utilizadas == (): # jogada inválida: tenta outra vez
                continue

            soma = 0 # é a soma dos pontos das letras
            for letra in palavra:
                if letra in pontos:
                    soma += pontos[letra]
            jog['pontos'] += soma # atualiza a pontuação

            
            for letra in utilizadas: # retira só as gastas e repõe
                retira_letra(jog['letras'], letra)
                if len(pilha) > 0:
                    distribui_letra(pilha, jog)
            return True
        continue # Se não for P, T ou J: inválido, repete


# 3.4.3 função scrabble:
def scrabble(jogadores, saco, pontos, seed):
    """
    Executa um jogo de SCRABBLE no terminal.
    Argumentos:
    Jogadores --> Inteiro
    jogadores: Número de jogadores (2 a 4).
    saco --> Dicionário
    saco: Conjunto de letras do saco.
    pontos --> Dicionário
    pontos: Pontos por letra.
    seed --> Inteiro
    seed: Estado inicial do gerador psudo-aleatório.
    Returns:
    Retorna Tuplo com pontuações finais de cada jogador por ordem.
    """
    if type(jogadores) != int or jogadores < 1 or jogadores > 4:
        raise ValueError('scrabble: argumentos inválidos') # valida n.º jogadores
    if type(saco) != dict or type(pontos) != dict: # valida tipos
        raise ValueError('scrabble: argumentos inválidos')
    if type(seed) != int or seed < 0:
        raise ValueError('scrabble: argumentos inválidos')
    
    if len(saco) == 0:
        raise ValueError('scrabble: argumentos inválidos')
    
    for l in saco: # verifica se todas as letras do saco têm pontuação
        if l not in LETRAS or l not in pontos:
            raise ValueError('scrabble: argumentos inválidos')
        if type(saco[l]) != int or saco[l] < 1:
            raise ValueError('scrabble: argumentos inválidos')
        
    i = 0
    while i < len(LETRAS):
        L = LETRAS[i]
        if L not in pontos or type(pontos[L]) != int or pontos[L] < 1:
            raise ValueError('scrabble: argumentos inválidos')
        i = i + 1

    print('Bem-vindo ao SCRABBLE.')
    tab = cria_tabuleiro() # cria tabuleiro vazio
    print(tabuleiro_para_str(tab)) # mostra tabuleiro
    saco = baralha_conjunto(saco, seed) # baralha o saco

    players = []
    for i in range(jogadores):
        player = cria_jogador(i + 1, 0, {}) # cria jogadores
        for i in range(7): # dá 7 letras iniciais
            distribui_letra(saco, player)
        players.append(player)
        print(jogador_para_str(player)) # Mostra no ecrã as informacoes do jogador (id, pontos e letras)

    comecou = True # 1.ª jogada
    terminou = False # indica fim do jogo
    passa = 0 # conta quantas vezes foi passada a jogada 

    # Enquanto o jogo ainda não tiver terminado, continuam as rondas
    while not terminou: # rondas
        for j in range(jogadores):
            jogador = players[j] # jogador atual
            jogada = processa_jogada(tab, jogador, saco, pontos, comecou)
            if obtem_valor(tab, (8, 8)) != '.': #  Se o centro do tabuleiro (8,8) já tiver sido ocupado, significa que a primeira jogada já aconteceu
                comecou = False
            if not jogada: # se passou a jogada
                passa = passa + 1
            else:
                passa = 0 # Se o jogador ja jogou, o contador reinicia

            # Condições de fim do jogo:
            # Todos os jogadores passaram a vez consecutivamente
            # O jogador atual ficou sem letras e o saco está vazio
            if passa == jogadores or (len(jogador['letras']) == 0 and len(saco) == 0):
                terminou = True # condição que marca o fim do ciclo
                break

            # Mostra o tabuleiro atualizado após a jogada
            print(tabuleiro_para_str(tab))

            # Mostra as informacoes atualizadas de todos os jogadores (pontuação e letras)
            for p in players:
                print(jogador_para_str(p))
    # Após terminar o jogo:
    pontuacoes = [] # compilacao das pontuações
    for p in players: # Percorre todos os jogadores e recolhe os pontos de cada um
        pontuacoes.append(p['pontos'])   
    return tuple(pontuacoes) # retorna o tuplo final com as pontuações finais, por ordem dos jogadores

