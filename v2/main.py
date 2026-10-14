from domain.Pedido import Pedido
from domain.FretePac import FretePac
from domain.FreteSedex import FreteSedex
from domain.FreteDrone import FreteDrone

def main():
    print("=== Sistema de E-commerce ===")
    
    # Simulação de um pedido feito no sistema
    peso_carrinho = 4.0
    meu_pedido = Pedido(peso_kg=peso_carrinho)
    print(f"Pedido finalizado. Peso total: {peso_carrinho} kg.")

    # O usuário seleciona o frete PAC no site
    print("\n-> Calculando envio via PAC...")
    meu_pedido.set_estrategia_frete(FretePac())
    print(f"Custo do frete: R$ {meu_pedido.calcular_frete():.2f}")

    # O usuário muda de ideia e seleciona SEDEX para chegar mais rápido
    print("\n-> Calculando envio via SEDEX...")
    meu_pedido.set_estrategia_frete(FreteSedex())
    print(f"Custo do frete: R$ {meu_pedido.calcular_frete():.2f}")

    # O usuário decide experimentar o envio via DRONE, que é uma nova opção de frete
    print("\n-> Calculando envio via DRONE...")
    meu_pedido.set_estrategia_frete(FreteDrone())
    print(f"Custo do frete: R$ {meu_pedido.calcular_frete():.2f}")

if __name__ == "__main__":
    main()