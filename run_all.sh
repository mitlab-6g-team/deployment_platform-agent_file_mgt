#!/bin/bash
# entrypoint: mitlab-6g-aiml-dashboard

source .env

docker network rm ${AIML_NETWORK_NAME}

# create network
docker network create ${AIML_NETWORK_NAME}

./shell/run_backend.sh \
    && docker network connect ${AIML_NETWORK_NAME} ${BACKEND_CONTAINER_NAME} \