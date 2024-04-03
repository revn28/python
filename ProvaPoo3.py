class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return litros_abastecidos
        else:
            print("Quantidade de combustível insuficiente.")
            return 0
    
    def abastecer_por_litro(self, litros):
        valor_abastecido = litros * self.valor_litro
        if litros <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros
            return valor_abastecido
        else:
            print("Quantidade de combustível insuficiente.")
            return 0
    
    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
    
    def alterar_combustivel(self, novo_tipo_combustivel, nova_quantidade):
        self.tipo_combustivel = novo_tipo_combustivel
        self.quantidade_combustivel = nova_quantidade
    
    def mostrar_combustivel(self):
        print(f"Tipo de Combustível: {self.tipo_combustivel}")
        print(f"Valor por Litro: {self.valor_litro}")
        print(f"Quantidade de Combustível: {self.quantidade_combustivel} litros")
        
    def abastecerPorValor(self, valor):
        litros_abastecidos = self.abastecer_por_valor(valor)
        if litros_abastecidos > 0:
            print(f"Abastecidos {litros_abastecidos:.2f} litros.")
            self.mostrar_combustivel() 
        else:
            print("Não foi possível realizar o abastecimento.")
    
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade



bomba1 = BombaCombustivel("Gasolina", 5.0, 1000)
bomba1.mostrar_combustivel()

print("\nAbastecendo 50 reais de gasolina:")
bomba1.abastecerPorValor(50)

print("\nAbastecendo 20 litros de gasolina:")
bomba1.abastecer_por_litro(20)

print("\nAlterando a quantidade de combustível:")
bomba1.alterarQuantidadeCombustivel(800)
bomba1.mostrar_combustivel()
