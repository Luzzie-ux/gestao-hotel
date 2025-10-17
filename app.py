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

def menu_clientes():
    """Menu de gestão de clientes"""
    while True:
        print("\n--- GESTÃO DE CLIENTES ---")
        print("[1] Adicionar cliente")
        print("[2] Listar clientes")
        print("[0] Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do cliente: ")
            email = input("Email: ")
            telefone = input("Telefone: ")
            adicionar_cliente(nome, email, telefone)
        elif opcao == "2":
            listar_clientes()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")

def menu_quartos():
    """Menu de gestão de quartos"""
    while True:
        print("\n--- GESTÃO DE QUARTOS ---")
        print("[1] Adicionar quarto")
        print("[2] Listar quartos")
        print("[3] Atualizar status do quarto")
        print("[0] Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            numero = input("Número do quarto: ")
            tipo = input("Tipo (Single/Double/Suite): ")
            preco = input("Preço por noite (€): ")
            try:
                adicionar_quarto(numero, tipo, float(preco))
            except ValueError:
                print("❌ Preço inválido!")
        elif opcao == "2":
            listar_quartos()
        elif opcao == "3":
            numero = input("Número do quarto: ")
            status = input("Novo status (disponível/ocupado): ")
            atualizar_status_quarto(numero, status)
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")

def menu_reservas():
    """Menu de gestão de reservas"""
    while True:
        print("\n--- GESTÃO DE RESERVAS ---")
        print("[1] Criar reserva")
        print("[2] Cancelar reserva")
        print("[3] Listar reservas")
        print("[0] Voltar")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            cliente_id = input("ID do cliente: ")
            quarto_numero = input("Número do quarto: ")
            data_entrada = input("Data de entrada (DD/MM/AAAA): ")
            data_saida = input("Data de saída (DD/MM/AAAA): ")
            criar_reserva(cliente_id, quarto_numero, data_entrada, data_saida)
        elif opcao == "2":
            reserva_id = input("ID da reserva: ")
            cancelar_reserva(reserva_id)
        elif opcao == "3":
            listar_reservas()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")