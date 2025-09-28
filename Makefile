.PHONY: build up down logs test

# Rebuilda as imagens sem cache
build:
	docker-compose build --no-cache

# Sobe a API Flask
up:
	docker-compose up web

# Derruba todos os containers
down:
	docker-compose down

# Mostra os logs
logs:
	docker-compose logs -f

# Roda os testes
test:
	docker-compose run --rm test
