from abc import ABC, abstractmethod

# Interface para a estratégia de cálculo de frete
class EstrategiaFrete(ABC):
    
    @abstractmethod
    def calcular_frete(self, pedido) -> float:
        pass