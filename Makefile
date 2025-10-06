# ==============================
# L5R Compendium - Dev Makefile
# ==============================

# Diretórios ignorados por padrão
EXCLUDES := --exclude .venv --exclude venv --exclude build --exclude __pycache__

# ==================================
# 🔧 Comandos principais de formatação
# ==================================

# 👉 Verifica formatação e tipos (sem alterar arquivos)
lint:
	@echo "🔍 Verificando código com Black, isort, Ruff e Mypy..."
	black --check .
	isort --check-only .
	ruff check .
	mypy .

# 👉 Corrige automaticamente estilo e lint
fix:
	@echo "🧹 Formatando e corrigindo código..."
	black .
	isort .
	ruff check --fix .

# 👉 Limpa arquivos temporários e caches
clean:
	@echo "🗑️ Limpando caches e pastas temporárias..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache .ruff_cache .pytest_cache

# 👉 Roda tudo de uma vez (fixa e depois valida)
all: fix lint

# ==================================
# 🧪 Outras utilidades
# ==================================

# 👉 Atualiza dependências
update:
	@echo "📦 Atualizando dependências..."
	pip install -U pip
	pip install -U -r requirements.txt

# 👉 Mostra versão dos formatadores
versions:
	@echo "🧰 Versões das ferramentas:"
	@black --version
	@isort --version
	@ruff --version
	@mypy --version
