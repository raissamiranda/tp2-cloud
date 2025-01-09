# Base image
FROM python:3.9-slim-bullseye

# Definir diretório de trabalho
WORKDIR /app

# Copiar dependências e instalá-las
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /folder

# Copiar o código do servidor
COPY server.py .

# Expor a porta usada pelo Flask
EXPOSE 52056

# Comando para rodar o servidor Flask
CMD ["python", "server.py"]