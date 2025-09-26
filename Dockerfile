FROM python:3.11-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos necessários
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação
COPY . .

# Expõe a porta
EXPOSE 5000

# Usa gunicorn em modo produção com apenas 1 worker (estável)
CMD ["gunicorn", "-b", "0.0.0.0:5000", "--workers=1", "app:create_app()"]