from domain.FreteMotoboy import FreteMotoboy
from domain.Pedido import Pedido
from domain.FreteSedex import FreteSedex
from domain.FretePac import FretePac
from domain.FreteTransportadora import FreteTransportadora
from domain.FreteDrone import FreteDrone

# Para executar os testes, rode esse comando na raiz do diretorio v2:
# python -m tests.teste_frete

def rodar_testes():
    print("--- Iniciando Testes de Cálculo de Frete ---")
    
    # 1. Instanciando o contexto (Pedido) com um peso de exemplo
    meu_pedido = Pedido(peso_kg=3.5)

    # 2. Testando o Frete SEDEX
    meu_pedido.set_estrategia_frete(FreteSedex())
    valor_sedex = meu_pedido.calcular_frete()
    print(f"Valor SEDEX: R$ {valor_sedex:.2f}")

    # 3. Testando o Frete PAC
    meu_pedido.set_estrategia_frete(FretePac())
    valor_pac = meu_pedido.calcular_frete()
    print(f"Valor PAC: R$ {valor_pac:.2f}")

    # 4. Testando o Frete TRANSPORTADORA
    meu_pedido.set_estrategia_frete(FreteTransportadora())
    valor_transportadora = meu_pedido.calcular_frete()
    print(f"Valor TRANSPORTADORA: R$ {valor_transportadora:.2f}")

    # 5. Testando o Frete MOTOBOY
    meu_pedido.set_estrategia_frete(FreteMotoboy())
    valor_motoboy = meu_pedido.calcular_frete()
    print(f"Valor MOTOBOY: R$ {valor_motoboy:.2f} (Taxa Fixa)")

    # 5. Testando o Frete DRONE
    meu_pedido.set_estrategia_frete(FreteDrone())
    valor_drone = meu_pedido.calcular_frete()
    print(f"Valor DRONE: R$ {valor_drone:.2f} (Taxa Fixa)")

if __name__ == "__main__":
    rodar_testes()