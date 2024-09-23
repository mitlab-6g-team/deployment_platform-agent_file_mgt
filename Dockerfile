FROM python:3.8.10

WORKDIR /app/agent_file_mgt

COPY . .

RUN apt-get update \
    && pip install -r /app/agent_file_mgt/requirements/local.txt