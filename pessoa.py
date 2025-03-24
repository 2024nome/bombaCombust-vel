class pessoa:
    nome = None
    idade = None
    peso = None
    altura = None

    def __init__(self, nome, idade, peso, altura):
        self.__altura = altura
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    def envelhecer(self, valor=1):
        if self.__idade <=21:
            self.crescer()
        self.__idade += valor

    def crescer(self, valor=0.05):
        self.__altura += valor

    def engordar(self, valor=1):
        self.__peso += valor 

    def emagrecer(self, valor=1):
        self.__peso -=valor 

    def dado(self):
        print(
            f"me chamo{self.__nome},tenho {self.__idade} anos, peso {self.__peso} quilos e tenho {self.__altura} de altura.\n\n prazer!"
        )

pessoa1 = pessoa('fabio', 28, 90, 1.75)