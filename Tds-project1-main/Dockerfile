# image-name : khushishahcreates/tdsproject1

# docker image url
# url = "https://hub.docker.com/r/khushishahcreates/tdsproject1"

FROM python:3.12-slim-bookworm

RUN apt-get update && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g prettier@3.4.2 \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
RUN apt-get update && apt-get install -y git

RUN git config --global user.name "Khushi Shah" && \
    git config --global user.email "23f2005471@ds.study.iitm.ac.in"

# Download and install uv
WORKDIR /app

COPY . /app
#COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

CMD uvicorn app:app --host 0.0.0.0 --port 8000 --reload --reload-exclude data --reload-exclude datagen.py

