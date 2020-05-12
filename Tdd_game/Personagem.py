class Personagem():
    def __init__(self):
        self.vida = 0

    def receber_dano(self, dano):
        var = self.vida == dano
        return var
