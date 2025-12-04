
import seletordetexto as f
from deep_translator import GoogleTranslator


idioma=None
traducao=""
def traduzir():
    global idioma
    idioma=None
    while True:
        try:
            linguagem_para_traduzir_o_texto = input("Digite o numero referente a lingua desejada\n1-Inglês\n2-Espanhol \n3-Japones \n4-Francês\n5-Alemão \n6-Italiano\n7-Portugues\nDIGITE: ")
            numero_escolhido =int(linguagem_para_traduzir_o_texto)

            if 1 <= numero_escolhido <=7:
                break
            else:
                print("O numero deve ser de 1 a 7 ")

        except ValueError:
            print(("Entrada Invalida, digite apenas um numero de 1 a 7.\n"))

    if numero_escolhido == 1 :
        idioma="en"
        print("Inglês foi a linguagem escolhida")
    elif numero_escolhido == 2:
        idioma="es"
        print("Espanhol foi a linguagem escolhida")
    elif numero_escolhido == 3:
        idioma="ja"
        print("Japones foi a linguagem escolhida")
    elif numero_escolhido == 4 :
        idioma="fr"
        print("Francês foi a linguagem escolhida")
    elif numero_escolhido == 5:
        idioma="de"
        print("Alemão foi a linguagem escolhida")
    elif numero_escolhido==6:
        idioma="it"
        print("Italiano foi a linguagem escolhida")
    elif numero_escolhido == 7:
        idioma="pt"
        print("Portugues foi a linguagem escolhida")


def funcao():
    global traducao
    f.definindo_o_teclado()
    texto_para_traduzir = f.texto

    traducao = GoogleTranslator(source='auto', target=f"{idioma}").translate(texto_para_traduzir)
    return traducao


# traduzir()
# while True:
#     funcao()

    # i = input("\nEnter para continuar ou digite 1 para sair:\n")
    # if i == "1":
    #     break


