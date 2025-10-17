"""
Módulo de gestão de clientes
Funções para adicionar, listar e gerir clientes do hotel
"""

# Base de dados de clientes (simulada com lista)
clientes = []

def adicionar_cliente(nome, email, telefone):
    """
    Adiciona um novo cliente ao sistema
    
    Args:
        nome (str): Nome completo do cliente
        email (str): Email do cliente
        telefone (str): Número de telefone
    
    Returns:
        dict: Dados do cliente adicionado
    """
    # Gerar ID único
    cliente_id = f"CLI{len(clientes) + 1:03d}"
    
    cliente = {
        "id": cliente_id,
        "nome": nome,
        "email": email,
        "telefone": telefone
    }
    
    clientes.append(cliente)
    print(f"✅ Cliente '{nome}' adicionado com sucesso! (ID: {cliente_id})")
    return cliente

def listar_clientes():
    """
    Lista todos os clientes registados no sistema
    """
    if not clientes:
        print("⚠️  Nenhum cliente registado.")
        return
    
    print("\n" + "="*70)
    print(f"{'ID':<10} {'Nome':<25} {'Email':<20} {'Telefone':<15}")
    print("="*70)
    
    for cliente in clientes:
        print(f"{cliente['id']:<10} {cliente['nome']:<25} {cliente['email']:<20} {cliente['telefone']:<15}")
    
    print("="*70)
    print(f"Total de clientes: {len(clientes)}")


def buscar_cliente(cliente_id):
    """
    Busca um cliente pelo ID
    
    Args:
        cliente_id (str): ID do cliente
    
    Returns:
        dict ou None: Dados do cliente ou None se não encontrado
    """
    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente
    return None

def remover_cliente(cliente_id):
    """
    Remove um cliente do sistema
    
    Args:
        cliente_id (str): ID do cliente a remover
    
    Returns:
        bool: True se removido, False caso contrário
    """
    cliente = buscar_cliente(cliente_id)
    if cliente:
        clientes.remove(cliente)
        print(f"✅ Cliente {cliente_id} removido com sucesso!")
        return True
    else:
        print(f"❌ Cliente {cliente_id} não encontrado!")
        return False