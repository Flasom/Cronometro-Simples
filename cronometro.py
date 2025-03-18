import time
from tkinter import *

tela = Tk()

class Temporizador():
    """Retorna o tempo em segundos e milisegundos"""

    def __init__(self):
        self.tempo_base = time.time()

    def get(self):
        seg_miliseg = time.time() - self.tempo_base
        return round(seg_miliseg, 3)

class Cronometro(Temporizador):
    """Cria a interface do cronometro"""

    def __init__(self):
        self.tela = tela
        self.parar = False
        self.conf_tela()
        self.frames()
        self.label()
        self.buttons()
        self.tela.mainloop()

    def conf_tela(self):
        self.tela.title("Cronômetro")
        self.tela.configure(background="#1C1C1C")
        self.tela.minsize(height=200, width=400)

    def frames(self):
        self.frame_1 = Frame(self.tela, bg="gray")
        self.frame_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.65)

        self.frame_2 = Frame(self.tela, bg="#1C1C1C")
        self.frame_2.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.2)

    def label(self):
        self.tempo = Label(self.frame_1, text="0", fg="white", bg="#1C1C1C",)
        self.tempo.place(relheight=1, relwidth=1)

    def atualizar_crono(self):
        self.tela.after(1, self.iniciar())

    def iniciar(self):
        pass
    
    def pare(self):
        if self.parar:
            self.parar = False
        else:
            self.parar = True

    def buttons(self):
        """Cria os botões da tela"""
        self.iniciar_button = Button(self.frame_2, text="iniciar", command=self.iniciar)
        self.iniciar_button.place(relx=0, relheight=1, relwidth=0.3)

        self.reiniciar_button = Button(self.frame_2, text="reiniciar", command=self.pare)
        self.reiniciar_button.place(relx=0.35, relheight=1, relwidth=0.3)

        self.parar_button = Button(self.frame_2, text="parar")
        self.parar_button.place(relx=0.70, relheight=1, relwidth=0.3)


Cronometro()
