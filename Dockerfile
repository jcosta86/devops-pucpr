# Usa uma imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos da aplicação para dentro do container
COPY . .

# (Opcional) Instala dependências, se você tiver um requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o app
CMD ["python", "main.py"]
