class bombaCombustível:
    tipoCombustiver = None
    ValorLitro = None
    quantidadeCombustivel = None


    def __init__(self, tipoCombustiver, ValorLitro, QuantidadeCombustiverl):
        self.__tipoCombustiver = tipoCombustiver
        self.__valorLitro = ValorLitro
        self.__quantidadeCombustivel = QuantidadeCombustiverl
        

    def abastecerPorValor(self, valor):
        litros = valor / self.__valorLitro
        if litro > self.__quantidadeCombustivel:
            print("quantidade insuficiente na bomba!")
            return
        
        self.__quantidadeCombustivel -= litros
        print(f"foram abastecidos{litros}")


    def abastecerPorLitro(self):
        pass

    def alterarValor(self):
        pass

    def alterarCombustivel(self):
        pass

    def QuantidadeCombustivel(self, valor= 200):
        pass


