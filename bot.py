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
    if navegador.find_element_by_link_text('Não foi possível se conectar ao Instagram. Verifique se você está conectado à Internet e tente novamente.').is_displayed():
        print('\nNão foi possível se conectar ao Instagram. Verifique se você está conectado à Internet e tente novamente.\n')
    else: 
        print('\nLogin efetuado com sucesso!\n')
        time.sleep(20)
        #Clicar no agora não
        try:
            navegador.find_elements_by_link_text('Agora não')[0].click()
        except:
            try:
                navegador.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
            except:
                print('\n[ERRO] Não foi possível clicar no agora não\n')

        time.sleep(2)

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
        try:
            navegador.find_element_by_xpath('/html/body/div[1]/section/div[3]/button/div/svg/line').click()
        except:
            try:
                navegador.find_element_by_class_name('wpO6b  ').click()
            except:
                try:
                    navegador.find_element_by_class_name('QBdPU ').click()
                except:
                    print('\n[ERRO] Não foi possível fechar storys\n')


if seguir_ou_movimentar == '1':
    seguir_curtir()
    print('Você selecionou 1')
    if quer_curtir == 's' or quer_curtir == 'S':
        curtir()
    if quer_seguir == 's' or quer_seguir == 'S':
        seguir()
    elif quer_curtir == 'n' and quer_seguir == 'n':
        print('Você não quer nada...')
elif seguir_ou_movimentar == '2':
    movimentar()
    print('Você selecionou 2')
else:
    print('Opção inválida!')





