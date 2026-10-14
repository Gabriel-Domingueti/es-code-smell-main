from domain.EstrategiaFrete import EstrategiaFrete

class FreteMotoboy(EstrategiaFrete):

    def calcular_frete(self, pedido) -> float:
        return 15.0