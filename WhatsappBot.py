from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import PySimpleGUI as Sg

#Layout

Sg.theme('DarkPurple2')


aviso = [
    [Sg.popup_ok('''                                    INSTRUÇÕES!
        
O primeiro campo é para colocar o nome para qual deseja enviar a mensagem(Colocar o mesmo nome que consta em seu whatsapp).
O segundo campo é o campo da mensagem.
O botão resetar retira todos os nomes dos contatos para envio.
Ao clicar em enviar, irá abrir a tela do whatsapp Web, você tem 30 segundos para escanear o qrcode para entrar no seu whatsapp, depois disso é só aguardar o envio da mensagem.
        ''', title='instruções',)]
]


layout = [
    [Sg.InputText(key='texto', do_not_clear=False), Sg.Button('Adicionar')],
    [Sg.Multiline(key='msg'), Sg.Button('Enviar')],
    [Sg.Button('Resetar')]
]
#Variaveis
contato = []
mensagem = ''

#fazer a pesquisa e entrar.
def pesquisar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div [contains(@class, "copyable-text selectable-text")]')
    sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)

window = Sg.Window('Bot Whatsapp', layout)

#Loop
while True:
    event, values = window.read()
    if event == 'Adicionar':
        a = values['texto']
        contato.append(a)
    elif event == 'Enviar':
        mensagem = values['msg']
        #Navergar até o site.
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://web.whatsapp.com')
        sleep(15)
        #Definir para quem vai enviar.
        for contato in contato:
            pesquisar_contato(contato)
            sleep(3)
            enviar_mensagem(mensagem)
    elif event == 'Resetar':
        resetado = ''
        contato = resetado
    elif event == Sg.WIN_CLOSED:
        break
