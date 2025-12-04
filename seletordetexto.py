import keyboard
import pyperclip
import time



atalho = 'ctrl+0'
texto=""
def texto_selecionado_para_traducao():
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.1)
    texto_selecionado = pyperclip.paste()
    global texto
    texto = texto_selecionado
    return texto









def definindo_o_teclado():

    keyboard.add_hotkey(atalho, texto_selecionado_para_traducao)

    keyboard.wait(atalho)


if __name__ == '__main__':
    definindo_o_teclado()


