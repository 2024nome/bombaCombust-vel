class bombaCombustivel:
    __tipoCombustivel = None
    __valorPorLitro = None
    __quantidadeCombustivel = None


    def __init__(self, tipoCombustivel, ValorPorLitro, quantidadeCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorPorLitro = ValorPorLitro
        self.__quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self,valor):
        litros = valor / self.__valorPorLitro
        if self.__quantidadeCombustivel >= litros:
            print(f"Abastecendo {litros:.2f} litros de {self.__tipoCombustivel} com valor do litro de {self.__valorPorLitro:.2f}")
            self.__quantidadeCombustivel -= litros
        else:
            print(f"infelizmente, não dipomos dessa quantidades de litros. Volte mais tarde!")

    def abastecerPorlitros(self, litros):
        valor = litros * self.__valorPorLitro
        if self.__quantidadeCombustivel >= litros:
            print(f"\n\n Abastecendo: {litros:.2f} litros.\nTipo combustível: {self.__tipoCombustivel}. \nValor do litro:{self.__valorPorLitro:.2f}.\nvalor total")
            self.__quantidadeCombustivel -= litros
        else:
            print("Infelizmente, não dispomos dessa quantidade de litros. volte mais tarde!")


    def alteraValor(self, novoValor):
        self.__valorPorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.__tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, novoQuantidade):
        self.__quantidadeCombustivel = novoQuantidade

    def __getTipoCombustivel__(self):
        return self.__tipoCombustivel
    
bomba = bombaCombustivel("gasolina comun", 6.8, 200)