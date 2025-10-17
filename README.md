# 🏨 Sistema de Gestão de Reservas de Hotel

## 📋 Descrição do Projeto

Sistema desenvolvido em Python para gestão completa de reservas, quartos e clientes de um hotel. Este projeto foi criado como parte da avaliação de controlo de versões com Git e GitHub, demonstrando boas práticas de desenvolvimento colaborativo.

## 👥 Autores

- Rodrigo da Luz
estelarodrigoluz@gmail.com

## ✨ Funcionalidades Principais

### 🧑‍💼 Gestão de Clientes
- ✅ Registar novos clientes com nome, email e telefone
- 📋 Listar todos os clientes registados
- 🔍 Buscar clientes por ID
- 🗑️ Remover clientes do sistema

### 🏠 Gestão de Quartos
- ✅ Adicionar quartos com número, tipo (Single/Double/Suite) e preço
- 📋 Listar todos os quartos disponíveis e ocupados
- 🔄 Atualizar status dos quartos (disponível/ocupado)
- 🔍 Verificar disponibilidade de quartos específicos
- 📊 Visualizar estatísticas de ocupação

### 📅 Gestão de Reservas
- ✅ Criar reservas associando clientes a quartos
- ❌ Cancelar reservas existentes
- 📋 Listar todas as reservas (ativas e canceladas)
- 🔍 Buscar reservas por ID
- 👤 Consultar reservas por cliente
- 🔄 Atualização automática do status dos quartos

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior instalado
- Git instalado

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/<seu-utilizador>/gestao-hotel-git.git
cd gestao-hotel-git
```

2. Execute o sistema:
```bash
python app.py
```

## 📂 Estrutura do Projeto

```
gestao-hotel-git/
├── app.py          # Aplicação principal com interface de menu
├── clientes.py     # Módulo de gestão de clientes
├── quartos.py      # Módulo de gestão de quartos
├── reservas.py     # Módulo de gestão de reservas
└── README.md       # Documentação do projeto
```

## 🔀 Workflow de Desenvolvimento

### Branches Utilizadas
- `main` - Branch principal com código estável
- `feature-clientes` - Desenvolvimento da gestão de clientes
- `feature-quartos` - Desenvolvimento da gestão de quartos
- `feature-reservas` - Desenvolvimento da gestão de reservas

### Convenções de Commits
- `feat:` - Nova funcionalidade
- `fix:` - Correção de bug
- `docs:` - Alterações na documentação
- `refactor:` - Refatoração de código
- `test:` - Adição ou modificação de testes

Exemplos:
```bash
git commit -m "feat: adiciona função de registo de clientes"
git commit -m "fix: corrige bug na validação de emails"
git commit -m "docs: atualiza README com instruções de instalação"
```

## 🧪 Exemplo de Uso

```python
# Adicionar um cliente
>>> adicionar_cliente("João Silva", "joao@email.com", "912345678")
✅ Cliente 'João Silva' adicionado com sucesso! (ID: CLI001)

# Adicionar um quarto
>>> adicionar_quarto("101", "Double", 80.00)
✅ Quarto 101 (Double) adicionado com sucesso!

# Criar uma reserva
>>> criar_reserva("CLI001", "101", "15/10/2025", "20/10/2025")
✅ Reserva RES001 criada com sucesso!
```

## 📊 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Controlo de Versões:** Git
- **Plataforma de Colaboração:** GitHub
- **Estrutura:** Programação modular com separação de responsabilidades

## 🤝 Como Contribuir

1. Faça fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'feat: adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais como parte da avaliação de Git e GitHub.

## 📞 Contacto

Para questões ou sugestões, contacte os autores através dos emails fornecidos acima.

---

**Versão:** v1.0  
**Data:** Outubro 2025  
**Instituição:** IEFP