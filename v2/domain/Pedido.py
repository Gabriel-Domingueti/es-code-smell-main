from domain.EstrategiaFrete import EstrategiaFrete

class Pedido:
    def __init__(self, peso_kg: float, estrategia_frete: EstrategiaFrete = None):
        self._peso_kg = peso_kg
        self._estrategia_frete = estrategia_frete

    def set_estrategia_frete(self, estrategia_frete: EstrategiaFrete):
        self._estrategia_frete = estrategia_frete

    # Definindo os Getters
    @property
    def peso_kg(self) -> float:
        return self._peso_kg

    @property
    def estrategia_frete(self) -> EstrategiaFrete:
        return self._estrategia_frete

    def calcular_frete(self) -> float:

        # Verifica se a estratégia de frete foi definida
        if not self._estrategia_frete:
            raise ValueError("Estratégia de frete não definida.")
        
        return self.estrategia_frete.calcular_frete(self)