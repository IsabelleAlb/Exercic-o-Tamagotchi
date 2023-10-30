class Pessoa:

    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.dormindo = False
        self.falando = False


    #método para mostrar se a ação é repetida e a mensagem certa
    def ocupado(self, igual, acao):
        string = ""
        if self.comendo:
            string = "já está comendo"
        elif self.falando:
            string = "já está falando"
        else:
            string = "já está dormindo"
        if igual:
            print(f"{self.nome}", string)
        else:
            print(f"{self.nome} nao pode {acao} porque", string)


    def comer(self, comida):
        if self.comendo == True or self.dormindo == True or self.falando == True:
            self.ocupado(self.comendo, "comer")
        else:
            print(f"{self.nome} foi comer {comida}")
            self.comendo = True
            self.action = f"{self.nome} já está comendo"

    def pararComer(self):
        if self.comendo == True:
            print(f"{self.nome} parou de comer")
            self.comendo = False
        else:
            print(f"{self.nome} não estava comendo")

    def dormir(self):
        if self.comendo == True or self.dormindo == True or self.falando == True:
            self.ocupado(self.dormindo, "dormir")
        else:
            print(f"{self.nome} foi dormir")
            self.dormindo = True
            self.action = f"{self.nome} já está dormindo"

    def acordar(self):
        if self.dormindo == True:
            print(f"{self.nome} acordou")
            self.dormindo = False
        else:
            print(f"{self.nome} já está acordado")

    def falar(self):
        if self.comendo == True or self.dormindo == True or self.falando == True:
            self.ocupado(self.falando, "falar")
        else:
            print(f"{self.nome} começou a falar")
            self.falando = True
            self.action = f"{self.nome} já está falando"

    def pararFalar(self):
        if self.falando == True:
            print(f"{self.nome} calou a boca")
            self.falando = False
        else:
            print(f"{self.nome} já está em silêncio")
