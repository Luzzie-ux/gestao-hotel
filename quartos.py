"""
Módulo de gestão de quartos
Funções para adicionar, listar e gerir quartos do hotel
"""

# Base de dados de quartos (simulada com lista)
quartos = []

def adicionar_quarto(numero, tipo, preco):
    """
    Adiciona um novo quarto ao sistema
    
    Args:
        numero (str): Número do quarto
        tipo (str): Tipo do quarto (Single, Double, Suite)
        preco (float): Preço por noite
    
    Returns:
        dict: Dados do quarto adicionado
    """
    # Verificar se o quarto já existe
    if buscar_quarto(numero):
        print(f"❌ Quarto {numero} já existe!")
        return None
    
    quarto = {
        "numero": numero,
        "tipo": tipo,
        "preco": preco,
        "status": "disponível"
    }
    
    quartos.append(quarto)
    print(f"✅ Quarto {numero} ({tipo}) adicionado com sucesso!")
    return quarto

def listar_quartos(filtro_status=None):
    """
    Lista todos os quartos do hotel
    
    Args:
        filtro_status (str, optional): Filtrar por status (disponível/ocupado)
    """
    quartos_filtrados = quartos
    
    if filtro_status:
        quartos_filtrados = [q for q in quartos if q["status"] == filtro_status]
    
    if not quartos_filtrados:
        print("⚠️  Nenhum quarto encontrado.")
        return
    
    print("\n" + "="*70)
    print(f"{'Número':<10} {'Tipo':<15} {'Preço/Noite':<15} {'Status':<15}")
    print("="*70)
    
    for quarto in quartos_filtrados:
        status_icon = "🟢" if quarto["status"] == "disponível" else "🔴"
        print(f"{quarto['numero']:<10} {quarto['tipo']:<15} €{quarto['preco']:<14.2f} {status_icon} {quarto['status']:<13}")
    
    print("="*70)
    print(f"Total de quartos: {len(quartos_filtrados)}")
    
    # Estatísticas
    disponiveis = len([q for q in quartos if q["status"] == "disponível"])
    ocupados = len([q for q in quartos if q["status"] == "ocupado"])
    print(f"Disponíveis: {disponiveis} | Ocupados: {ocupados}")

def buscar_quarto(numero):
    """
    Busca um quarto pelo número
    
    Args:
        numero (str): Número do quarto
    
    Returns:
        dict ou None: Dados do quarto ou None se não encontrado
    """
    for quarto in quartos:
        if quarto["numero"] == numero:
            return quarto
    return None

def atualizar_status_quarto(numero, novo_status):
    """
    Atualiza o status de um quarto
    
    Args:
        numero (str): Número do quarto
        novo_status (str): Novo status (disponível/ocupado)
    
    Returns:
        bool: True se atualizado, False caso contrário
    """
    if novo_status not in ["disponível", "ocupado"]:
        print("❌ Status inválido! Use 'disponível' ou 'ocupado'.")
        return False
    
    quarto = buscar_quarto(numero)
    if quarto:
        quarto["status"] = novo_status
        print(f"✅ Status do quarto {numero} atualizado para '{novo_status}'!")
        return True
    else:
        print(f"❌ Quarto {numero} não encontrado!")
        return False

def verificar_disponibilidade(numero):
    """
    Verifica se um quarto está disponível
    
    Args:
        numero (str): Número do quarto
    
    Returns:
        bool: True se disponível, False caso contrário
    """
    quarto = buscar_quarto(numero)
    return quarto and quarto["status"] == "disponível"