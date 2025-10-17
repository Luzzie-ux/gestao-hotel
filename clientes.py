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