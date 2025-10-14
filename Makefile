# ==============================
# L5R Compendium - Dev Makefile
# ==============================

# Default directories to ignore
EXCLUDES := --exclude .venv --exclude venv --exclude build --exclude __pycache__

# ==================================
# 🔧 Main Formatting and Lint Commands
# ==================================

# 👉 Check formatting and types (without modifying files)
lint:
	@echo "🔍 Checking code with Black, isort, Ruff, and Mypy..."
	black --check .
	isort --check-only .
	ruff check .
	mypy .

# 👉 Automatically fix style and lint issues
fix:
	@echo "🧹 Formatting and fixing code..."
	black .
	isort .
	ruff check --fix .

# 👉 Clean up temporary files and caches
clean:
	@echo "🗑️ Cleaning caches and temporary folders..."
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache .ruff_cache .pytest_cache

# 👉 Run everything at once (fix, then validate)
all: fix lint

# ==================================
# 🧪 Additional Utilities
# ==================================

# 👉 Update dependencies
update:
	@echo "📦 Updating dependencies..."
	pip install -U pip
	pip install -U -r requirements.txt

# 👉 Show versions of formatting tools
versions:
	@echo "🧰 Tool versions:"
	@black --version
	@isort --version
	@ruff --version
	@mypy --version
