from re import I
from selenium import webdriver
import time

print('\n--------BOT--------')
user = input('Perfil: ')
senha = input('Senha: ')
quer_curtir = input('Curtir posts do arquivo posts_a_curtir.txt? (s/n) ')
quer_seguir = input('Seguir perfis do arquivo perfis_a_seguir.txt? (s/n) ')

def seguir():
    print('Vou seguir...')
    
    #criar navegador
    navegador = webdriver.Chrome('chromedriver.exe')

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
    
    #criar navegador
    navegador = webdriver.Chrome('chromedriver.exe')

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
if quer_seguir == 's' or quer_seguir == 'S':
    seguir()
elif quer_curtir == 'n' and quer_seguir == 'n':
    print('Você não quer nada...')