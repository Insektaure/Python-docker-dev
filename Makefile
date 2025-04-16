SHELL = /bin/sh

# Build for either x86 or ARM
CHIPSET_ARCH := `[ "$(shell uname -m)" = "arm64" ] && echo "aarch64-linux-gnu" || echo "x86_64-linux-gnu"`

CURRENT_UID := $(shell id -u)
CURRENT_GID := $(shell id -g)

export CURRENT_UID
export CURRENT_GID

COMPOSE = docker compose -f docker-compose.yml

all:
	@echo "..."

# -------------------------------------
# Starter
# -------------------------------------
pre-up:
	@echo "=========================================="
	@echo "Current user id: ${CURRENT_UID}"
	@echo "Current group id: ${CURRENT_GID}"
	@echo "Target architecture: ${CHIPSET_ARCH}"
	@echo "=========================================="

build:
	@$(COMPOSE) build --build-arg CHIPSET_ARCH=$(CHIPSET_ARCH)

up: pre-up
	@$(COMPOSE) up -d

down:
	@$(COMPOSE) down -v --rmi local

stop:
	@$(COMPOSE) stop

status:
	$(COMPOSE) ps

# -------------------------------------
# Builders
# -------------------------------------
setup: pre-up build up
	@$(COMPOSE) exec php composer install --working-dir=/var/www