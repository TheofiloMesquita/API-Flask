# Usa a imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos de dependência
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Variáveis de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Expõe a porta
EXPOSE 5000

# Comando padrão para rodar o Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]