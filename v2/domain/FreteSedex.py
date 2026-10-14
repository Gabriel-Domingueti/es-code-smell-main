from domain.EstrategiaFrete import EstrategiaFrete

class FreteSedex(EstrategiaFrete):

    def calcular_frete(self, pedido) -> float:
        return 10.0 + (pedido.peso_kg * 1.5)