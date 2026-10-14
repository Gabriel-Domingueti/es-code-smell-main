from domain.EstrategiaFrete import EstrategiaFrete

class FretePac(EstrategiaFrete):

    def calcular_frete(self, pedido) -> float:
        return 5.0 + (pedido.peso_kg * 1.0)