"""
Sistema de Gestão de Reservas de Hotel
Aplicação principal com menu interativo
"""

from clientes import adicionar_cliente, listar_clientes, clientes
from quartos import adicionar_quarto, listar_quartos, atualizar_status_quarto, quartos
from reservas import criar_reserva, cancelar_reserva, listar_reservas, reservas

def mostrar_menu():
    """Apresenta o menu principal do sistema"""
    print("\n" + "="*50)
    print("  SISTEMA DE GESTÃO DE RESERVAS DE HOTEL")
    print("="*50)
    print("\n[1] Gestão de Clientes")
    print("[2] Gestão de Quartos")
    print("[3] Gestão de Reservas")
    print("[0] Sair")
    print("-"*50)

