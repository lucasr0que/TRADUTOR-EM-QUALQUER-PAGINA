import traduzirv2 as t
import interface as i
import seletordetexto as s
import keyboard

import subprocess
import sys

s.atalho="ctrl+ç"
reiniciar="alt+ç"
i.resposta=t.traducao
def reiniciar_programa():#Isso aqui volta pra escolher a linguagem
    subprocess.Popen([sys.executable] + sys.argv)
    sys.exit()
def iniciar():
    print(f"Atalho para traduzir {s.atalho}\nTrocar linguagem {reiniciar}\n")
    t.traduzir()
    while True:
        t.funcao()
        i.resultado_da_traducao(t.traducao)

keyboard.add_hotkey(reiniciar,reiniciar_programa)
iniciar()



