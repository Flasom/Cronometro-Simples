import time
class Temporizador():
    """Retorna o tempo em segundos e milisegundos"""
    def __init__(self):
        self.tempo_base = time.time()

    def get(self):
        seg_miliseg = time.time() - self.tempo_base
        return round(seg_miliseg, 4)

t = Temporizador()

while True:
    print(t.get())