class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano     

    def descrever(self):
        return f"marca: {self.marca}, modelo:{self.modelo}, ano: {self.ano}"

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano ):
        super().__init__(marca, modelo, ano)

    

class Moto(Veiculo): 
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)

    

class Caminhão(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo, ano)
            

carro = Carro("Ford", "Fusion", 2005)
moto = Moto("Honda", "CBR", 1997)
caminhão = Caminhão("daf", "XF", 2004)

print(carro.descrever())
print(moto.descrever())
print(caminhão.descrever())
