from domain.EstrategiaFrete import EstrategiaFrete

class FreteTransportadora(EstrategiaFrete):

    def calcular_frete(self, pedido) -> float:
        return 20.0 + (pedido.peso_kg * 3.0)