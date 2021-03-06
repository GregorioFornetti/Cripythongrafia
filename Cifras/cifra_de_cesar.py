import Cifras.utilidades_cifras as utilidades
import dicionarios

def retorna_chave_se_for_valida(lista_chaves):  # Função validadora da chave.
    if lista_chaves[0].isnumeric():
        return lista_chaves[0]
    return False


def encriptar_modo_apenas_letras(lista_chaves, mensagem):
    chave = retorna_chave_se_for_valida(lista_chaves)
    return mensagem_nova_modo_apenas_letras(chave, mensagem)


def traduzir_modo_apenas_letras(lista_chaves, mensagem):
    chave = adaptar_chave_para_traduçao_apenas_letras(lista_chaves)
    return mensagem_nova_modo_apenas_letras(chave, mensagem)


def mensagem_nova_modo_apenas_letras(chave, mensagem):
    if not mensagem:
        return dicionarios.retorna_erro_mensagem()
    if chave:
        return cesar_troca_apenas_letras(chave, mensagem)
    else:
        return dicionarios.retorna_erro_chave()


def adaptar_chave_para_traduçao_apenas_letras(lista_chaves):  # Adaptar a chave para a tradução, caso ela seja válida.
    chave = retorna_chave_se_for_valida(lista_chaves)
    if chave:
        chave = utilidades.TAMANHO_ALFABETO - (int(chave) % utilidades.TAMANHO_ALFABETO)
    return chave


def cesar_troca_apenas_letras(chave, mensagem):
    mensagem_nova = ''
    chave = int(chave) % utilidades.TAMANHO_ALFABETO  # Diminuir o valor da chave para o número de letras existentes no alfabeto.
    for letra in mensagem:
        ascii_letra = ord(letra)
        ascii_soma = ascii_letra + chave
        if ascii_letra >= utilidades.MIN_MINUSCULA and ascii_letra <= utilidades.MAX_MINUSCULA:
            if ascii_soma > utilidades.MAX_MINUSCULA:
                ascii_soma -= utilidades.TAMANHO_ALFABETO  # O codigo ascii passou de 'z', então deve voltar ao inicio.
            mensagem_nova += chr(ascii_soma)
        elif ascii_letra >= utilidades.MIN_MAIUSCULA and ascii_letra <= utilidades.MAX_MAIUSCULA:  # Criptografia para letras maiusculas.
            if ascii_soma > utilidades.MAX_MAIUSCULA:
                ascii_soma -= utilidades.TAMANHO_ALFABETO  # O codigo ascii passou de 'Z', então deve voltar ao inicio.
            mensagem_nova += chr(ascii_soma)
        else:
            mensagem_nova += letra  # Caso a mensagem tenha caracteres especiais ou caracteres com acentos, eles serão adicionados sem mudanças.
    return mensagem_nova


def encriptar_modo_varios_caracteres(lista_chaves, mensagem):
    dic_unicode = utilidades.criar_dicionario_caracteres_imprimiveis(utilidades.FINAL_UNICODE)
    chave = retorna_chave_se_for_valida(lista_chaves)
    return mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode)


def traduzir_modo_varios_caracteres(lista_chaves, mensagem):
    dic_unicode = utilidades.criar_dicionario_caracteres_imprimiveis(utilidades.FINAL_UNICODE) 
    chave = adaptar_chave_para_traduçao_varios_caracteres(lista_chaves, dic_unicode)
    return mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode)


def mensagem_nova_modo_varios_caracteres(chave, mensagem, dic_unicode):
    if not mensagem:
        return dicionarios.retorna_erro_mensagem()
    if chave:
        return cesar_troca_varios_caracteres(chave, mensagem, dic_unicode)
    else:
        return dicionarios.retorna_erro_chave()


def cesar_troca_varios_caracteres(chave, mensagem, dic_unicode):
    tot_caracteres_imprimiveis = len(dic_unicode) // 2
    chave = int(chave) % tot_caracteres_imprimiveis
    nova_mensagem = ''
    for letra in mensagem:
        if ord(letra) <= utilidades.FINAL_UNICODE:  # Caractere está dentro do limite.
            valor_unicode_nova_letra = dic_unicode[letra] + chave
            if valor_unicode_nova_letra >= tot_caracteres_imprimiveis:
                valor_unicode_nova_letra -= tot_caracteres_imprimiveis
            nova_mensagem += dic_unicode[valor_unicode_nova_letra]
        else:  # Caractere está fora do limite, colocar ele sem mudanças.
            nova_mensagem += letra
    return nova_mensagem


def adaptar_chave_para_traduçao_varios_caracteres(lista_chaves, dic_unicode):
    tot_utilidades_imprimiveis = len(dic_unicode) // 2
    chave = retorna_chave_se_for_valida(lista_chaves)
    if chave:
        chave = tot_utilidades_imprimiveis - (int(chave) % tot_utilidades_imprimiveis)
    return chave
