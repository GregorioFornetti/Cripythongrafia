import valores


def testa_chave_vigenere(chave):  # Função que testa se a chave fornecida pelo usuário é válida.
    chave = chave.lower().replace(' ', '')  # Apagar todos os espaços da chave.
    if chave.isalpha():  # Depois de retirar todos os espaços, verificar se o usuário digitou apenas letras.
        return chave
    return False
    

def vigenere(chave, mensagem, modo_traducao=False):  # Função que traduz/encripta a mensagem pela cifra de Vigenère.
    if not mensagem:  # Se o usuário não escreveu uma mensagem, retornar uma mensagem de erro !
        return 'Mensagem inválida !'
    if modo_traducao:
        chave = cria_chave_traducao(chave)
    else:
        chave = testa_chave_vigenere(chave)
    tamanho_chave = len(chave)
    if chave:
        valor_atual_chave = 0
        mensagem_encriptada = ''
        for letra in mensagem:
            letra_cifrada = letra
            letra_ASCII = ord(letra)  # Valor ASCII da letra atual da mensagem.
            chave_ASCII = ord(chave[valor_atual_chave]) - valores.MIN_MINUSCULA  # Valor alfabético (0-25, A=0, B=1,...) da letra da chave atual. 
            if letra_ASCII >= valores.MIN_MINUSCULA and letra_ASCII <= valores.MAX_MINUSCULA:  # Casos de letras minusculas.
                letra_ASCII -= valores.MIN_MINUSCULA
                index_alfabeto = (letra_ASCII + chave_ASCII) % 26  # Juntar os valores da letra da chave e da mensagem. (OBS: não pode passar de 26, que é o mesmo que dar uma volta no alfabeto).
                letra_cifrada = valores.ALFABETO_MINUSCULO[index_alfabeto]  # Pegar a letra com o valor alfabético calculado pelo index_alfabeto.
                valor_atual_chave += 1  # Mover a letra da chave em uma casa.
            elif letra_ASCII >= valores.MIN_MAIUSCULA and letra_ASCII <= valores.MAX_MAIUSCULA:  # Casos de letras maiusculas.
                letra_ASCII -= valores.MIN_MAIUSCULA
                index_alfabeto = (letra_ASCII + chave_ASCII) % 26
                letra_cifrada = valores.ALFABETO_MAIUSCULO[index_alfabeto]
                valor_atual_chave += 1  # Mover a letra da chave em uma casa.
            mensagem_encriptada += letra_cifrada
            if valor_atual_chave >= tamanho_chave:  # Se a chave chegou ao final, voltar para o início.
                valor_atual_chave = 0
    else:  # Se a chave é inválida, retornar uma mensagem de erro.
        return 'Chave inválida !'
    return mensagem_encriptada         


def cria_chave_traducao(chave):  # Função que adapta a chave para a tradução.
    chave = testa_chave_vigenere(chave)
    if chave:
        chave_traduc = ''
        for letra in chave:
            letra_ASCII = ord(letra) - valores.MIN_MINUSCULA
            if letra_ASCII == 0:
                chave_traduc += valores.ALFABETO_MINUSCULO[0]
                continue
            letra_atual = 26 - letra_ASCII  # Para transformar a chave, basta subtrair 26 com o antigo valor da chave (isso fará com que a mensagem de uma "volta" e volte ao normal).
            chave_traduc += valores.ALFABETO_MINUSCULO[letra_atual]
        return chave_traduc
    else:
        return 'Chave inválida !'


def cria_chave_traducao_varias_letras(chave):
    '''
    Função que cria a chave de tradução de vigenere para várias letras.
    A função recebe como parâmetro uma chave, que será adaptada para a tradução.
    '''
    chave_traduc = []
    for letra in chave:  # Adaptando a chave.
        # Cada letra da nova chave tem um código que completa o valor da chave antiga até chegar a dar uma volta.
        ASCII_atual = ord(letra)
        novo_valor = (valores.TAMANHO_ASCII - (ASCII_atual % valores.TAMANHO_ASCII))
        chave_traduc.append(novo_valor)
    return chave_traduc


def vigenere_varias_letras(chave, mensagem, modo_traducao=False):
    '''
    Função que encriptará a mensagem com a cifra de vigenere no modo várias letras.
    Recebe como parâmetros uma chave (string), mensagem(string) e modo_traducao(bool).
    '''
    if not mensagem:
        return 'Mensagem inválida !'
    chave_atual = 0
    if chave:
        tamanho_chave = len(chave)
        if modo_traducao:  # A mensagem deve ser traduzida, então encaminhar todas as informaçôes para a função de tradução.
           return traduz_vigenere_varia_letras(chave, mensagem, tamanho_chave, chave_atual)
        mensagem_nova = ''
        for letra in mensagem:
            chave_ASCII = ord(chave[chave_atual]) % valores.TAMANHO_ASCII
            letra_ASCII = ord(letra) + chave_ASCII
            if letra_ASCII > valores.FINAL_ASCII - valores.TAMANHO_ESPAÇO_VAZIO:  # Valor passou do valor final, então é hora de voltar para o início da tabela.
                letra_ASCII -= (valores.VOLTAR_PARA_INICIO - valores.TAMANHO_ESPAÇO_VAZIO)
            if letra_ASCII >= valores.INICIO_VAZIO:  # Passou da região vazia, então deve receber 34 ao seu valor final.
                letra_ASCII += valores.TAMANHO_ESPAÇO_VAZIO
            chave_atual += 1  # Atualizar index da chave.
            if chave_atual >= tamanho_chave:  # Voltar ao inicio da chave caso a chave passe de seu valor máximo.
                chave_atual = 0
            mensagem_nova += chr(letra_ASCII)
        return mensagem_nova
    else:
        return 'Chave inválida !'


def traduz_vigenere_varia_letras(chave, mensagem, tamanho_chave, valor_atual):
    '''
    Função que traduzirá a cifra de vigenere no moodo várias letras.
    Recebe como parâmetro "chave" a antiga chave utilizada para encriptar.
    Mensagem é uma string contendo um texto encriptado.
    Tamanho da chave é a quantidade de caracteres presente na chave.
    Valor atual é um int = 0.
    '''
    chave_traduc = cria_chave_traducao_varias_letras(chave)  # Coletar a chave de tradução.
    mensagem_traduzida = ''
    for letra in mensagem:
        letra_msg_atual = ord(letra)
        letra_ASCII = letra_msg_atual + chave_traduc[valor_atual]
        verificar_volta = letra_msg_atual - ord(chave[valor_atual])
        if letra_msg_atual > valores.INICIO_VAZIO and verificar_volta - valores.TAMANHO_ESPAÇO_VAZIO < valores.INICIO_ASCII:
            # Antiga letra na mensagem recebeu 34 a mais para sua pontuação, então precisa corrigir agora para a tradução.
            letra_ASCII -= valores.TAMANHO_ESPAÇO_VAZIO
        if letra_msg_atual < valores.INICIO_VAZIO and verificar_volta > valores.INICIO_ASCII:
            letra_ASCII += valores.TAMANHO_ESPAÇO_VAZIO
        if letra_ASCII > valores.FINAL_ASCII:  # Chegou ao valor final da tabela, então é hora de voltar ao início da tabela.
            letra_ASCII -= valores.VOLTAR_PARA_INICIO
        valor_atual += 1  # Atualizar index da chave.
        if valor_atual >= tamanho_chave:  # Voltar ao inicio da chave caso a chave passe de seu valor máximo.
            valor_atual = 0
        mensagem_traduzida += chr(letra_ASCII)
    return mensagem_traduzida