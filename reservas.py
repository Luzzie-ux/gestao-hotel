"""
Módulo de gestão de reservas
Funções para criar, cancelar e listar reservas
"""

from clientes import buscar_cliente
from quartos import buscar_quarto, atualizar_status_quarto, verificar_disponibilidade

# Base de dados de reservas (simulada com lista)
reservas = []

def criar_reserva(cliente_id, quarto_numero, data_entrada, data_saida):
    """
    Cria uma nova reserva
    
    Args:
        cliente_id (str): ID do cliente
        quarto_numero (str): Número do quarto
        data_entrada (str): Data de entrada
        data_saida (str): Data de saída
    
    Returns:
        dict: Dados da reserva criada ou None se falhar
    """
    # Validar cliente
    cliente = buscar_cliente(cliente_id)
    if not cliente:
        print(f"❌ Cliente {cliente_id} não encontrado!")
        return None
    
    # Validar quarto
    quarto = buscar_quarto(quarto_numero)
    if not quarto:
        print(f"❌ Quarto {quarto_numero} não encontrado!")
        return None
    
    # Verificar disponibilidade
    if not verificar_disponibilidade(quarto_numero):
        print(f"❌ Quarto {quarto_numero} não está disponível!")
        return None
    
    # Gerar ID único para a reserva
    reserva_id = f"RES{len(reservas) + 1:03d}"
    
    reserva = {
        "id": reserva_id,
        "cliente_id": cliente_id,
        "cliente_nome": cliente["nome"],
        "quarto_numero": quarto_numero,
        "data_entrada": data_entrada,
        "data_saida": data_saida,
        "status": "ativa",
        "preco_total": quarto["preco"]
    }
    
    reservas.append(reserva)
    
    # Atualizar status do quarto para ocupado
    atualizar_status_quarto(quarto_numero, "ocupado")
    
    print(f"✅ Reserva {reserva_id} criada com sucesso!")
    print(f"   Cliente: {cliente['nome']}")
    print(f"   Quarto: {quarto_numero}")
    print(f"   Período: {data_entrada} até {data_saida}")
    
    return reserva

def cancelar_reserva(reserva_id):
    """
    Cancela uma reserva existente
    
    Args:
        reserva_id (str): ID da reserva
    
    Returns:
        bool: True se cancelada, False caso contrário
    """
    reserva = buscar_reserva(reserva_id)
    
    if not reserva:
        print(f"❌ Reserva {reserva_id} não encontrada!")
        return False
    
    if reserva["status"] == "cancelada":
        print(f"⚠️  Reserva {reserva_id} já estava cancelada!")
        return False
    
    # Atualizar status da reserva
    reserva["status"] = "cancelada"
    
    # Liberar o quarto
    atualizar_status_quarto(reserva["quarto_numero"], "disponível")
    
    print(f"✅ Reserva {reserva_id} cancelada com sucesso!")
    print(f"   Quarto {reserva['quarto_numero']} agora está disponível.")
    
    return True

def listar_reservas(filtro_status=None):
    """
    Lista todas as reservas
    
    Args:
        filtro_status (str, optional): Filtrar por status (ativa/cancelada)
    """
    reservas_filtradas = reservas
    
    if filtro_status:
        reservas_filtradas = [r for r in reservas if r["status"] == filtro_status]
    
    if not reservas_filtradas:
        print("⚠️  Nenhuma reserva encontrada.")
        return
    
    print("\n" + "="*100)
    print(f"{'ID':<10} {'Cliente':<20} {'Quarto':<10} {'Entrada':<12} {'Saída':<12} {'Status':<12} {'Preço':<10}")
    print("="*100)
    
    for reserva in reservas_filtradas:
        status_icon = "✅" if reserva["status"] == "ativa" else "❌"
        print(f"{reserva['id']:<10} {reserva['cliente_nome']:<20} {reserva['quarto_numero']:<10} "
              f"{reserva['data_entrada']:<12} {reserva['data_saida']:<12} "
              f"{status_icon} {reserva['status']:<10} €{reserva['preco_total']:.2f}")
    
    print("="*100)
    print(f"Total de reservas: {len(reservas_filtradas)}")
    
    # Estatísticas
    ativas = len([r for r in reservas if r["status"] == "ativa"])
    canceladas = len([r for r in reservas if r["status"] == "cancelada"])
    print(f"Ativas: {ativas} | Canceladas: {canceladas}")

def buscar_reserva(reserva_id):
    """
    Busca uma reserva pelo ID
    
    Args:
        reserva_id (str): ID da reserva
    
    Returns:
        dict ou None: Dados da reserva ou None se não encontrada
    """
    for reserva in reservas:
        if reserva["id"] == reserva_id:
            return reserva
    return None

def listar_reservas_cliente(cliente_id):
    """
    Lista todas as reservas de um cliente específico
    
    Args:
        cliente_id (str): ID do cliente
    """
    reservas_cliente = [r for r in reservas if r["cliente_id"] == cliente_id]
    
    if not reservas_cliente:
        print(f"⚠️  Cliente {cliente_id} não possui reservas.")
        return
    
    print(f"\nReservas do cliente {cliente_id}:")
    listar_reservas()