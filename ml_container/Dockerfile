# Base image
FROM python:3.9-slim-bullseye

# Diretório de trabalho
WORKDIR /app

# Dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /folder

# Copiar o código do gerador de regras
COPY rule_generator.py .

# Comando para rodar o gerador de regras
CMD ["python", "rule_generator.py"]

RUN ls /app
RUN ls .

# O comando docker build -t ml_container:1.0 . é usado para construir uma imagem Docker a partir de um Dockerfile localizado no diretório atual.
# Ele instrui o Docker a processar as instruções definidas no Dockerfile, como definir a imagem base, copiar arquivos, instalar dependências e configurar o ambiente.
# Durante o processo, o Docker cria uma imagem nomeada como ml_container e marcada com a versão 1.0.
# Essa imagem contém o ambiente configurado e os arquivos necessários para executar uma aplicação ou serviço, permitindo que seja usada posteriormente para rodar containers.


# Pra atualizar a tag no quay.io
# docker build -t quay.io/raissamaciel/ml-container:3.0 .
# docker push quay.io/raissamaciel/ml-container:3.0

# docker build -t quay.io/raissamaciel/frontend-container:2.0 .
# docker push quay.io/raissamaciel/frontend-container:2.0

# kubectl -n raissamaciel delete job ml-job
# kubectl -n raissamaciel apply -f ml-deployment.yaml
# kubectl -n raissamaciel apply -f frontend-deployment.yaml
# kubectl -n raissamaciel apply -f service.yaml

# wget --server-response \
# --output-document response.out \
# --header='Content-Type: application/json' \
# --post-data '{"songs": ["HUMBLE.", "DNA.", "Bad and Boujee (feat. Lil Uzi Vert)"]}' \
# http://<CLUSTER-IP>:52056/api/recommend
