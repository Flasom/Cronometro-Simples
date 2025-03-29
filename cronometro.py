import time
from tkinter import *
from tkinter.font import Font

tela = Tk()


class Temporizador():
    """Retorna o tempo em segundos e milisegundos"""

    def __init__(self):
        self.tempo_base = time.time()

    def get(self):
        self.seg_miliseg = time.time() - self.tempo_base
        return round(self.seg_miliseg, 4)

    def get_pause(self):
        return time.time()


class Cronometro(Temporizador):
    """Cria a interface do cronometro"""

    def __init__(self):
        self.tela = tela
        self.parar = False
        self.milisegundos, self.segundos, self.minutos, self.horas = 0, 0, 0, 0
        self.diminuidor = 1
        self.conf_tela()
        self.frames()
        self.atualizar_tela("00:00:00.00")
        self.buttons()
        self.tela.mainloop()

    def conf_tela(self):
        """Armazena as configurações da tela"""
        self.tela.title("Cronômetro")
        self.tela.configure(background="#1C1C1C")
        self.tela.geometry("400x200")
        self.tela.resizable(width=False, height=False)

    def frames(self):
        """Cria as partições da tela"""
        self.frame_1 = Frame(self.tela, bg="gray")
        self.frame_1.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.65)

        self.frame_2 = Frame(self.tela, bg="#1C1C1C")
        self.frame_2.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.2)

    def atualizar_tela(self, tempo):
        """Atualiza o tempo na tela"""
        self.tempo = Label(self.frame_1, text=tempo,
                           fg="white", bg="#1C1C1C", font=Font(size=50))
        self.tempo.place(relheight=1, relwidth=1)

    def formatador_tempo(self):
        """Formata o calculo do tempo para formato de horas"""
        if self.milisegundos < 10:
            self.t_milisegundos = "0" + str(self.milisegundos)
        else:
            self.t_milisegundos = self.milisegundos
        if self.segundos < 10:
            self.t_segundos = "0" + str(self.segundos)
        else:
            self.t_segundos = self.segundos
        if self.minutos < 10:
            self.t_minutos = "0" + str(self.minutos)
        else:
            self.t_minutos = self.minutos
        if self.horas < 10:
            self.t_horas = "0" + str(self.horas)
        else:
            self.t_horas = self.horas

        tempo_formatado = f"{self.t_horas}:{self.t_minutos}:{self.t_segundos}.{self.t_milisegundos}"
        self.atualizar_tela(tempo_formatado)
        self.tela.after(2, self.calc_tempo)

    def calc_tempo(self):
        """Calcula o tempo corrido"""
        if self.parar == False:
            self.segs_milis = self.cronometro.get()
            if self.segs_milis < self.diminuidor:
                if self.segs_milis > 1:
                    self.milisegundos = round(
                        (self.segs_milis - (self.diminuidor - 1)) / 9.999 * 1000)
                else:
                    self.milisegundos = round((self.segs_milis/9.999*1000))
            else:
                self.segundos += 1
                self.diminuidor += 1
            if self.segundos >= 60:
                self.segundos -= 60
                self.minutos += 1
            if self.minutos >= 60:
                self.minutos -= 60
                self.horas += 1
            self.formatador_tempo()

    def iniciar(self):
        """Inicia o cronometro"""
        if self.parar == False:
            self.cronometro = Temporizador()
        elif self.parar == 'reset':
            self.parar = False
            self.iniciar()
        else:
            try:
                self.cronometro.tempo_base = (
                    time.time() - self.diminuidor + 1) - (self.milisegundos * 9.999 / 1000)
                self.parar = False
            except:
                self.parar = False
                self.iniciar()
        self.calc_tempo()

    def pare(self):
        """Para o cronômetro"""
        self.parar = True
        try:
            self.parado = self.cronometro.get_pause()
        except:
            pass

    def reiniciar(self):
        """Reinicia o cronômetro"""
        self.parado = 0
        self.milisegundos = 0
        self.segundos = 0
        self.minutos = 0
        self.horas = 0
        self.diminuidor = 1
        self.parar = "reset"
        self.atualizar_tela("00:00:00.00")

    def buttons(self):
        """Cria os botões da tela"""
        self.iniciar_button = Button(
            self.frame_2, text="iniciar", command=self.iniciar)
        self.iniciar_button.place(relx=0, relheight=1, relwidth=0.3)

        self.reiniciar_button = Button(
            self.frame_2, text="reiniciar", command=self.reiniciar)
        self.reiniciar_button.place(relx=0.35, relheight=1, relwidth=0.3)

        self.parar_button = Button(
            self.frame_2, text="parar", command=self.pare)
        self.parar_button.place(relx=0.70, relheight=1, relwidth=0.3)


Cronometro()
