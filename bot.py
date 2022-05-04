from re import I
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

#Ler o user e senha
user = None
senha = None
with open('perfil_instagram.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    for perfil in linhas:
        user = perfil.split(',')[0]
        senha = perfil.split(',')[1]

print('\n--------BOT--------')
seguir_ou_movimentar = '2'#input('Seguir/curtir ou movimentar? (Digite 1 ou 2) ')

if seguir_ou_movimentar == '1':
    print('\nVocê digitou 1!')
    quer_curtir = input('Curtir posts do arquivo posts_a_curtir.txt? (s/n) ')
    quer_seguir = input('Seguir perfis do arquivo perfis_a_seguir.txt? (s/n) ') 

def seguir_curtir():
    def seguir():
        print('Vou seguir...')
        #iniciar navegador firefox estando no linux
        navegador = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        #criar navegador
        #navegador = webdriver.Chrome('chromedriver.exe')

        #entrar no site do instagram
        navegador.get('https://www.instagram.com/')
        time.sleep(5)

        #preencher usuário
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)

        #preencher senha
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
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
        navegador.close()
    def curtir():
        print('Vou curtir...')
        
        #iniciar navegador firefox estando no linux
        navegador = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        #criar navegador
        #navegador = webdriver.Chrome('chromedriver.exe')

        #entrar no site do instagram
        navegador.get('https://www.instagram.com/')
        time.sleep(5)

        #preencher usuário
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)

        #preencher senha
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
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
                navegador.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button').click() #click no coração de seguir
                print('Curti!')
                time.sleep(5)
                
        print('Já curti todos da lista!')

    if quer_curtir == 's' or quer_curtir == 'S':
        curtir()
    else:
        print('[ERRO]: Opção inválida!')

    if quer_seguir == 's' or quer_seguir == 'S':
        seguir()
    else:
        print('[ERRO]: Opção inválida!')

def movimentar():
    tempo_storys = input('Tempo de movimentação (minutos): ')
    tempo_storys = int(tempo_storys)
    tempo_storys = tempo_storys * 60
    print(tempo_storys)
    #iniciar navegador firefox estando no linux
    navegador = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    #entrar no site do instagram
    navegador.get('https://www.instagram.com/')
    time.sleep(5)

    #preencher usuário
    navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(user)

    #preencher senha
    navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
    time.sleep(2)

    #clicar no botão entrar
    try:
        navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    except:
        pass

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

    #clicar no segundo agora não ERRO AQUI
    try:
        #selecionar elemento pelo texto 'Agora não'
        navegador.find_element_by_link_text('Agora não').click()
    except:
        try:
            navegador.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        except:
            print('\n[ERRO] Não foi possível clicar no segundo agora não\n')


    #Assistir Storys por 5 minutos usando a classe do elemento
    print('\nAssistindo Storys por 5 minutos\n')
    try:
        navegador.find_element_by_class_name('Fd_fQ ').click()
    except:
        try:
            navegador.find_element_by_class_name('class="OE3OK "').click()
        except:
            print('\n[ERRO] Não foi possível assistir storys\n')
    
    time.sleep(tempo_storys)

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

    #rolar a página
    nova_altura = navegador.execute_script('return document.body.scrollHeight')
    print('nova_altura')
    navegador.execute_script('window.scrollTo(0, 500')


if seguir_ou_movimentar == '1':
    if quer_curtir == 'n' and quer_seguir == 'n':
        print('Você não quer curtir nem seguir ninguém!')
    seguir_curtir()
if seguir_ou_movimentar == '2':
    print('Iniciando movimentação...')
    movimentar()
else:
    print('Opção inválida!')
