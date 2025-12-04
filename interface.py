import tkinter as tk

cor_do_fundo = "#FFFFFF"
cor_do_texto = "#000000"


def resultado_da_traducao(resposta):
    janela = tk.Tk()  # serve pra criar uma janela

    janela.overrideredirect(True)  # serve pra tirar os botoes

    janela.configure(bg=cor_do_fundo)

    configuracoes = tk.Label(
        janela,
        text=resposta,
        bg=cor_do_fundo,
        fg=cor_do_texto,
        pady=5,
        padx=10,
    )
    configuracoes.pack()

    janela.update_idletasks() #aqui calcula tamanho da tela

    def fechar_a_janela(event):  # não tirar esse event se nao da erro no codigo
        janela.destroy()

    janela.bind("<Button-1>", fechar_a_janela)  # aqui eu defini q o botão esquerdo vai fechar a janela
    janela.bind("<Button-3>", fechar_a_janela)  # aqui é o botão direito
    janela.focus_force()  # esse aqui forca o debaixo a respeitar o codigo
    janela.bind("<FocusOut>", fechar_a_janela)  # esse aqui entende q qualuqer foco fora da janela ela vai fechar

    def posicao():


        largura_tela = janela.winfo_screenwidth()#pega o tamanho largura tela
        altura_tela = janela.winfo_screenheight()#pega o tamanho altura tela

        largura_janela = janela.winfo_width() #pega o tamanho da janela
        altura_janela = janela.winfo_height()


        mouse_x = janela.winfo_pointerx()#posicao x do mouse horizontal
        mouse_y = janela.winfo_pointery()#posicao y do mouse vertical

        distancia_do_cursor = 10  # distancia da janela pro mouse em px


        if mouse_x + largura_janela + distancia_do_cursor > largura_tela:
            posicao_x = mouse_x - largura_janela - distancia_do_cursor
        else:
            posicao_x = mouse_x + distancia_do_cursor


        if mouse_y + altura_janela + distancia_do_cursor > altura_tela:
            posicao_y = mouse_y - altura_janela - distancia_do_cursor
        else:
            posicao_y = mouse_y + distancia_do_cursor

        janela.geometry(f"+{posicao_x}+{posicao_y}")


    janela.after(20, posicao)

    janela.attributes("-topmost", True)  # isso aqui serve para deixar a janela acima de outra janela
    janela.mainloop()

resposta=""
# resultado_da_traducao(resposta)