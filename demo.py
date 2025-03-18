class Therian():
    """Cria um cachorro"""
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.raca = especie

    def latir(self):
        print("Au! Au!")
        

rex = Therian("Rex", 2, "PItbull")

print(rex.nome)
print(rex.idade)
print(rex.raca)

rex.latir()