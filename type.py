class BombaCombustivel:
    precos_combustiveis = {
        "Gasolina": 5.00,
        "Etanol": 4.00,
        "Diesel": 3.80
    }

    def __init__(self, tipo_combustivel, quantidade_combustivel):
        if tipo_combustivel not in self.precos_combustiveis:
            raise ValueError("Tipo de combustível inválido!")
        
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = self.precos_combustiveis[tipo_combustivel]
        self.__quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros = valor / self.__valor_litro
        if litros > self.__quantidade_combustivel:
            print("Quantidade insuficiente na bomba!")
            return
        
        self.__quantidade_combustivel -= litros
        print(f"Foram abastecidos {litros:.2f} litros de {self.__tipo_combustivel}.")

    def abastecer_por_litro(self, litros):
        valor_a_pagar = litros * self.__valor_litro
        if litros > self.__quantidade_combustivel:
            print("Quantidade insuficiente na bomba!")
            return
        
        self.__quantidade_combustivel -= litros
        print(f"O valor a ser pago é R$ {valor_a_pagar:.2f} para {litros:.2f} litros de {self.__tipo_combustivel}.")

    def alterar_combustivel(self, novo_tipo):
        if novo_tipo not in self.precos_combustiveis:
            print("Tipo de combustível inválido!")
            return
        
        self.__tipo_combustivel = novo_tipo
        self.__valor_litro = self.precos_combustiveis[novo_tipo]
        print(f"Combustível alterado para {novo_tipo}, novo valor por litro: R$ {self.__valor_litro:.2f}")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.__quantidade_combustivel = nova_quantidade

    def mostrar_dados(self):
        print(f"Combustível: {self.__tipo_combustivel}")
        print(f"Valor por litro: R$ {self.__valor_litro:.2f}")
        print(f"Quantidade na bomba: {self.__quantidade_combustivel:.2f} litros")


bomba = BombaCombustivel("Gasolina", 100.0)
bomba.mostrar_dados()
bomba.abastecer_por_valor(50)
bomba.abastecer_por_litro(10)
bomba.alterar_combustivel("Etanol")
bomba.abastecer_por_valor(40)
bomba.mostrar_dados()
