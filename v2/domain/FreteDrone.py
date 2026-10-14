from domain.EstrategiaFrete import EstrategiaFrete

class FreteDrone(EstrategiaFrete):

    def calcular_frete(self, pedido) -> float:
        return 25.0