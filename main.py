import PySimpleGUI as sg
import webbrowser
import testes_simples
import Cifras.cifra_de_cesar as cifra_de_cesar
import Cifras.cifra_de_vigenere as cifra_de_vigenere
import Cifras.subst_simples as subst_simples
import Menus.menus_utilitarios as menus_utilitarios
import Menus.menus_cifras as menus_cifras

sg.theme('DarkGrey5')
lista_criptografias_disponiveis = ['Cifra de César', 'Substituição simples', 'Cifra de Vigenère']
lista_utilitarios_disponiveis = ['Força bruta César', 'Adivinhador César']
dic_opçoes_disponiveis = {'Cifra de César': ['apenas letras', 'vários caracteres'],
                          'Substituição simples':['apenas letras', 'vários caracteres'],
                          'Cifra de Vigenère':['apenas letras', 'vários caracteres']}
dic_links = {'Cifra de César':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-C%C3%A9sar',
            'Substituição simples':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-substitui%C3%A7%C3%A3o-simples',
            'Cifra de Vigenère':'https://github.com/GregorioFornetti/Programa-criptografia/wiki/Cifra-de-Vigen%C3%A8re',
            'Wiki':'https://github.com/GregorioFornetti/Cripythongrafia/wiki',
            'Testes':'https://github.com/GregorioFornetti/Cripythongrafia/wiki/Op%C3%A7%C3%B5es-do-menu#4--testes-automatizados'}

def main():
    # Layout da interface principal do programa.
    layout_principal =  [[sg.Text('       Cripythongrafia: Tela principal')],
                        [sg.Button('1- Criar mensagem criptografada', key='1')],
                        [sg.Button('2- Traduzir mensagem criptografada', key='2')],
                        [sg.Button('3- Utilitários', key='3')],
                        [sg.Button('4- Exemplos de funcionalidades e testes', key='4')],
                        [sg.Button('5- Ajuda', key='5')],
                        [sg.Button('6- Finalizar programa', key='6')]]
    # Criar a interface principal do programa, utilizando o layout a cima.
    tela_principal = sg.Window('Cripythongrafia: Tela principal',layout_principal)
    while True:  # Loop que verifica cada interação do usuário com o programa.
        evento, valores = tela_principal.read()
        if evento in ('6', None):
            # Fechar o programa
            tela_principal.close()
            break
        if evento == '1':
            # Iniciar interface "encriptar".
            tela_principal.Hide()
            menu_encriptar(tela_principal)
        if evento == '2':
            # Iniciar a interface "traduzir".
            tela_principal.Hide()
            menu_traducao(tela_principal)
        if evento == '3':
            # Inicar interface "utilitários"
            tela_principal.Hide()
            menu_utilitarios(tela_principal)
        if evento == '4':
            # Iniciar a interface "testes automatizados".
            tela_principal.Hide()
            menu_testes(tela_principal)
        if evento == '5':
            # Abrir wiki ajuda
            webbrowser.open(dic_links['Wiki'])


def cria_layout_opcoes_enumeradas(titulo, lista_opcoes):
    layout = [[sg.Text(titulo)]]
    for n, opcao in enumerate(lista_opcoes):
        layout.append([sg.Button(f'{n + 1} - {opcao}', key=opcao)])
    layout.append([sg.Button('Retornar', key='retornar')])
    return layout


def retorna_layout_opçoes(criptografia):
    layout_opçoes = []
    for opçao in dic_opçoes_disponiveis[criptografia]:
        if not layout_opçoes:  # Definir a primeira opção como "default".
            layout_opçoes.append(sg.Radio(opçao, criptografia, key=opçao, default=True))
        else:
            layout_opçoes.append(sg.Radio(opçao, criptografia, key=opçao, default=False))
    return layout_opçoes


def retorna_layout_padrao_traduçao(titulo, criptografia):
    layout = [[sg.Text(titulo)],
             [sg.Text('Opções:')],
             retorna_layout_opçoes(criptografia),
             [sg.Text('Mensagem encriptada:'), sg.InputText(key='mensagem')],
             [sg.Text('Chave:'), sg.InputText(key='chave')],
             [sg.Text('Mensagem traduzida:')],
             [sg.Output(size=(75,25), key='output')],
             [sg.Button('Traduzir', key='traduzir'), sg.Button('Abrir guia da cifra', key='link'),
              sg.Button('Limpar tela', key='limpar') ,sg.Button('Retornar', key='retornar')]]
    return layout


def retorna_layout_padrao_encriptaçao(titulo, criptografia):
    layout = [[sg.Text(titulo)],
             [sg.Text('Opções:')],
             retorna_layout_opçoes(criptografia),
             [sg.Text('Mensagem:'), sg.InputText(key='mensagem')],
             [sg.Text('Chave:'), sg.InputText(key='chave')],
             [sg.Text('Mensagem encriptada:')],
             [sg.Output(size=(75,25), key='output')],
             [sg.Button('Encriptar', key='encriptar'), sg.Button('Abrir guia da cifra', key='link'),
              sg.Button('Limpar tela', key='limpar'), sg.Button('Retornar', key='retornar')]]
    return layout


def menu_encriptar(tela_anterior):
    layout_encriptar = cria_layout_opcoes_enumeradas('Cripythografia: Menu encriptação', lista_criptografias_disponiveis)
    tela_encriptar = sg.Window('Cripythongrafia: Menu encriptação', layout_encriptar)
    while True:
        evento, valores = tela_encriptar.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_encriptar)
            break
        tela_encriptar.Hide()
        if evento == 'Cifra de César':
            menus_cifras.menu_cifra_de_cesar_encriptação(tela_encriptar)
            #menu_cesar_encriptar(tela_encriptar)
        elif evento == 'Substituição simples':
            menu_subst_simples_encriptar(tela_encriptar)
        else:
            menu_vigenere_encriptar(tela_encriptar)


def menu_traducao(tela_anterior):
    layout_traduzir = cria_layout_opcoes_enumeradas('Cripythongrafia: Menu tradução', lista_criptografias_disponiveis)
    tela_traduzir = sg.Window('Cripythongrafia: Menu tradução', layout_traduzir)
    while True:
        evento, valores = tela_traduzir.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_traduzir)
            break
        tela_traduzir.Hide()
        if evento == 'Cifra de César':
            menu_cesar_traduzir(tela_traduzir)
        elif evento == 'Substituição simples':
            menu_subst_simples_traduzir(tela_traduzir)
        else:
            menu_vigenere_traduzir(tela_traduzir)


def menu_cesar_encriptar(tela_anterior):
    layout_cesar_encript = retorna_layout_padrao_encriptaçao(f"{'Cripythongrafia: Cifra de César (encriptação)':^110}", 'Cifra de César')
    tela_cesar_encript = sg.Window('Cripythongrafia: Cifra de César', layout_cesar_encript)
    while True:
        evento, valores = tela_cesar_encript.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_cesar_encript)
            break
        verificar_eventos_gerais('Cifra de César', evento, tela_cesar_encript)
        if evento == 'encriptar':
            if valores['apenas letras']:
                print(cifra_de_cesar.encriptar_modo_apenas_letras(valores['chave'], valores['mensagem']))
            else:
                print(cifra_de_cesar.encriptar_modo_varios_caracteres(valores['chave'], valores['mensagem']))


def menu_cesar_traduzir(tela_anterior):
    layout_cesar_traduc = retorna_layout_padrao_traduçao(f"{'Cripythongrafia: Cifra de César (tradução)':^110}", 'Cifra de César')
    tela_cesar_traduc = sg.Window('Cripythongrafia: Cifra de César', layout_cesar_traduc)
    while True:
        evento, valores = tela_cesar_traduc.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_cesar_traduc)
            break
        verificar_eventos_gerais('Cifra de César', evento, tela_cesar_traduc)
        if evento == 'traduzir':
            if valores['apenas letras']:
                print(cifra_de_cesar.traduzir_modo_apenas_letras(valores['chave'], valores['mensagem']))
            else:
                print(cifra_de_cesar.traduzir_modo_varios_caracteres(valores['chave'], valores['mensagem']))


def menu_subst_simples_encriptar(tela_anterior):
    # Criando o layout da substituição simples.
    layout_subst_encript = retorna_layout_padrao_encriptaçao(f"{'Cripythongrafia: Substituição simples (encriptação)':^110}", 'Substituição simples')
    layout_subst_encript = organiza_layout_subst_simples(layout_subst_encript)
    tela_subst_encript = sg.Window('Cripythongrafia: substituição simples', layout_subst_encript)
    while True:
        evento, valores = tela_subst_encript.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_subst_encript)
            break
        verificar_eventos_gerais('Substituição simples', evento, tela_subst_encript)
        if evento == 'encriptar':
            if valores['apenas letras']:
                print(subst_simples.executar_modo_apenas_letras(valores['chave_1'], valores['chave_2'], valores['mensagem']))
            else:
                print(subst_simples.executar_modo_varios_caracteres(valores['chave_1'], valores['chave_2'], valores['mensagem']))


def menu_subst_simples_traduzir(tela_anterior):
    layout_subst_traduc = retorna_layout_padrao_traduçao(f"{'Cripythongrafia: Substituição simples (tradução)':^110}", 'Substituição simples')
    layout_subst_traduc = organiza_layout_subst_simples(layout_subst_traduc)
    tela_subst_traduc = sg.Window('Cripythongrafia: substituição simples', layout_subst_traduc)
    while True:
        evento, valores = tela_subst_traduc.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_subst_traduc)
            break
        verificar_eventos_gerais('Substituição simples', evento, tela_subst_traduc)
        if evento == 'traduzir':
            if valores['apenas letras']:
                print(subst_simples.executar_modo_apenas_letras(valores['chave_2'], valores['chave_1'], valores['mensagem']))
            else:
                print(subst_simples.executar_modo_varios_caracteres(valores['chave_2'], valores['chave_1'], valores['mensagem']))


def organiza_layout_subst_simples(layout):
    # Trocará o nome do que era "chave" para "letras mensagem encriptada" e adicionará outro local para digitar chamado "letras mensagem comum".
    del layout[4]
    layout.insert(4, [sg.Text('Letras mensagem comum:    '), sg.Input('abcdefghijklmnopqrstuvwxyz', key='chave_1')])
    layout.insert(5, [sg.Text('Letras mensagem encriptada:'), sg.Input(key='chave_2')])
    return layout


def menu_vigenere_encriptar(tela_anterior):
    layout_vigenere_encript = retorna_layout_padrao_encriptaçao(f"{'Cripythongrafia: Cifra de Vigenère (encriptação)':^110}", 'Cifra de Vigenère')
    tela_vigenere_encript = sg.Window('Cripythongrafia: Cifra de Vigenère', layout_vigenere_encript)
    while True:
        evento, valores = tela_vigenere_encript.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_vigenere_encript)
            break
        verificar_eventos_gerais('Cifra de Vigenère', evento, tela_vigenere_encript)
        if evento == 'encriptar':
            if valores['apenas letras']:
                print(cifra_de_vigenere.encriptar_modo_apenas_letras(valores['chave'], valores['mensagem']))
            else:
                print(cifra_de_vigenere.encriptar_modo_varios_caracteres(valores['chave'], valores['mensagem']))


def menu_vigenere_traduzir(tela_anterior):
    layout_vigenere_traduc = retorna_layout_padrao_traduçao(f"{'Cripythongrafia: Cifra de Vigenère (tradução)':^110}", 'Cifra de Vigenère')
    tela_vigenere_traduc = sg.Window('Cripythongrafia: Cifra de Vigenère', layout_vigenere_traduc)
    while True:
        evento, valores = tela_vigenere_traduc.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_vigenere_traduc)
            break
        verificar_eventos_gerais('Cifra de Vigenère', evento, tela_vigenere_traduc)
        if evento == 'traduzir':
            if valores['apenas letras']:
                print(cifra_de_vigenere.traduzir_modo_apenas_letras(valores['chave'], valores['mensagem']))
            else:
                print(cifra_de_vigenere.traduzir_modo_varios_caracteres(valores['chave'], valores['mensagem']))


def menu_testes(tela_anterior):
    layout_testes = [[sg.Text(f"{'Cripythongrafia: Testes automatizados':^110}")],
                    [sg.Text('Clique em "testar" para iniciar alguns testes nas cifras disponíveis no programa.')],
                    [sg.Text('Além disso, você pode utilizar esses testes como exemplos para entender melhor\nsobre o funcionamento das cifras.')],
                    [sg.Output(size=(75,25), key='output')],
                    [sg.Button('Testar',key='testar'), sg.Button('Limpar tela', key='limpar'),
                     sg.Button('Acessar guia', key='link'), sg.Button('Retornar',key='retornar')]]

    tela_testes = sg.Window('Cripythongrafia: Testes automatizados', layout_testes)
    while True:
        evento, valores = tela_testes.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_testes)
            break
        verificar_eventos_gerais('Testes', evento, tela_testes)
        if evento == 'testar':
            # O usuário clicou em "testar".
            testes_simples.testar()


def menu_utilitarios(tela_anterior):
    layout_utilitarios = cria_layout_opcoes_enumeradas('Cripythongrafia: Menu utilitários', lista_utilitarios_disponiveis)
    tela_utilitarios = sg.Window('Cripythongrafia: Menu utilitários', layout_utilitarios)
    while True:
        evento, valores = tela_utilitarios.read()
        if evento in ('retornar', None):
            voltar_para_tela_anterior(tela_anterior, tela_utilitarios)
            break
        tela_utilitarios.Hide()
        if evento == 'Força bruta César':
            menus_utilitarios.menu_forca_bruta_cesar(tela_utilitarios)
        if evento == 'Adivinhador César':
            menus_utilitarios.menu_adivinhador_cesar(tela_utilitarios)


def voltar_para_tela_anterior(tela_anterior, tela_atual):  # Volta para a tela anterior se usuário escolheu botão "retornar".
    tela_anterior.UnHide()
    tela_atual.Close()


def verificar_eventos_gerais(nome_opcao, evento, tela_atual):  # Verifica e executa eventos disponiveis nos menus das cifras.
    if evento == 'link':
        webbrowser.open(dic_links[nome_opcao])
    elif evento == 'limpar':
        tela_atual.element('output').update('')


main()