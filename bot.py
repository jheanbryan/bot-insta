from calendar import c
from curses import KEY_END, KEY_MARK
from re import I
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

print('\n[INSTRUÇÕES]:\n')
print('1. Crie um arquivo com o nome "perfis_a_seguir.txt" e adicione os perfis que você deseja seguir.\n')
print('2. Crie um arquivo com o nome "posts_a_curtir.txt" e adicione os links dos posts que você deseja curtir.\n')
print('\nOS COMANDOS PASSADOS POR VOCÊ, SERÃO FEITOS EM TODAS AS CONTAS!\n')

print('\n--------BOT--------')
seguir_ou_movimentar = input('Seguir/curtir ou movimentar? (Digite 1 ou 2) ')
if seguir_ou_movimentar == '1':
    print('\nVocê digitou 1!')
    quer_curtir = input('Curtir posts do arquivo posts_a_curtir.txt? (s/n) ')
    quer_seguir = input('Seguir perfis do arquivo perfis_a_seguir.txt? (s/n) ') 

#iniciar navegador firefox estando no linux
navegador = webdriver.Firefox(executable_path=GeckoDriverManager().install())
user = None
senha = None

def seguir_curtir():
    def seguir():
        print('Vou seguir...')
        #entrar no site do instagram
        navegador.get('https://www.instagram.com/')
        time.sleep(5)

        #preencher usuário
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)
        
        #preencher senha
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
        print('\nPerfil Selecionado: {}\n'.format(user))
        time.sleep(2)

        #clicar no botão entrar
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(5)

        with open('perfis_a_seguir.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for perfis in linhas:       
                #digitar perfil a ser seguido
                navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(perfis)
                time.sleep(5)

                #clicar no nome do perfil a seguido (entrar nele)
                navegador.find_element_by_class_name('-qQT3').click()
                time.sleep(5)

                #clicar no botão de seguir
                navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/div/div/div/span/span[1]/button').click()
                print('Perfil seguido: ' + perfis)
                time.sleep(15)

        print('Já segui todos da lista!')
        time.sleep(5)

    def curtir():
        print('Vou curtir...')
        #entrar no site do instagram
        navegador.get('https://www.instagram.com/')
        time.sleep(5)

        #preencher usuário
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)

        #preencher senha
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
        print('\nPerfil Selecionado: {}\n'.format(user))
        time.sleep(2)

        #clicar no botão entrar
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        time.sleep(10)
        
        #clicar na barra de pesquisa
        navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]/div').click()
        time.sleep(2)
        with open('posts_a_curtir.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            for link in linhas:
                navegador.get(link)
                time.sleep(5)
                navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click() #click no coração de curtir
                print('Curti!')
                time.sleep(5)
                
        print('Já curti todos da lista!')
        
    if quer_curtir == 's' or quer_curtir == 'S':
        curtir()
    else:
        print('\n[ERRO]: Opção inválida!\n')

    if quer_seguir == 's' or quer_seguir == 'S':
        seguir()
    else:
        print('\n[ERRO]: Opção inválida!\n')

def movimentar():
    tempo_storys = input('Tempo de movimentação (minutos): ')
    tempo_storys = int(tempo_storys)
    tempo_storys = tempo_storys * 60
    print(tempo_storys)
    
    #entrar no site do instagram
    navegador.get('https://www.instagram.com/')
    time.sleep(5)

    #preencher usuário
    navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)

    #preencher senha
    navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
    print('\nPerfil Selecionado: {}\n'.format(user))
    time.sleep(2)

    #clicar no botão entrar
    try:
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    except:
        print('[ERRO]: Não foi possível entrar no perfil!')

    time.sleep(5)
    print('\nLogin efetuado com sucesso!\n')
    time.sleep(20)

    #Clicar no agora não ou ir para o feed
    try:
        navegador.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
    except:
        try:
            navegador.find_element_by_link_text('Agora não').click()
        except:
            print('\n[ERRO] Não foi possível clicar no agora não\n')

    time.sleep(2)

    #clicar no segundo agora não
    try:
        #selecionar elemento pelo texto 'Agora não'
        navegador.find_element_by_link_text('Agora não').click()
    except:
        try:
            navegador.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        except:
            print('\n[ERRO] Não foi possível clicar no segundo agora não\n')


    #Assistir Storys 
    print('\nAssistindo Storys por {} segundos\n'.format(tempo_storys))
    try:
        navegador.find_element_by_class_name('Fd_fQ ').click()
    except:
        try:
            navegador.find_element_by_class_name('class="OE3OK "').click()
        except:
            print('\n[ERRO] Não foi possível assistir storys\n')

    time.sleep(2)
    time.sleep(tempo_storys)
 
    #verificar se existe elemento com texto AO VIVO
    try:
        if navegador.find_element_by_xpath('/html/body/div[1]/section/div/div/div[1]/div/div[2]/div/header/div/div[2]/span').is_displayed() == True:
            print('\nÉ uma Live\n')
            try:
                #Voltar para a guia anterior com o navegador.back()
                navegador.back()
                time.sleep(2)
                navegador.refresh()
                time.sleep(10)
            except:
                print('\n[ERRO] ao fechar a live\n')
    except:
        print('\n[ERRO] Ao rolar storys pro lado, ou não é live\n')

    #Fechar storys
    print('\nFechando Storys\n')
    try:
        navegador.find_element_by_xpath('/html/body/div[1]/section/div[3]/button').click()
    except:
        try:
            navegador.find_element_by_xpath('/html/body/div[1]/section/div[3]/button/div').click()
        except:
            try:
                navegador.find_element_by_class_name('QBdPU ').click()
            except:
                try:
                    navegador.find_element_by_xpath('/html/body/div[1]/section/div[3]/button/div/svg').click()
                except:
                    try:
                        navegador.find_element_by_xpath('/html/body/div[1]/section/div[3]/button/div/svg/polyline').click()
                    except:
                        try:
                            navegador.find_element_by_xpath('/html/body/div[1]/section/div[3]/button/div/svg/line').click()
                        except:
                            try:
                                navegador.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/button/div/svg/line[1]').click()
                            except:
                                print('\n[ERRO] Não foi possível fechar storys\n')

    #rolar a página para baixo
    print('\nRolando a página para baixo\n')
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

with open('perfil_instagram.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for perfil in linhas:
        user = perfil.split(',')[0]
        senha = perfil.split(',')[1]

        #identei pra dentro, tava na margem
        if seguir_ou_movimentar == '1':
            if quer_curtir == 'n' and quer_seguir == 'n':
                print('\nVocê não quer curtir nem seguir ninguém!\n')
            seguir_curtir() #como se fosse o else
        elif seguir_ou_movimentar == '2':
            print('\nIniciando movimentação...\n')
            movimentar()
        else:
            print('\nOpção inválida!\n')

        print('\nFinalizando...\n')
        navegador.close()

