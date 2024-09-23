- # AI/ML Platform: aiml-oom/file-mgt
  The project is for the 6G NSTC(also called MOST). In the project, we offer automatic AI model training and deployment on the AI/ML platform we design.
- ## Goal

  The goal of the project is to build a control panel on ORAN RIC to control the automatic model training or deployment on the xApp/rApp.

- ## Developer
  - ahjayzz

- ## System Architeture
  - Backend Framework
    - Django:4.1.3
  - NFS Manager
    - Minio:latest

- ## How to run the project ?

  - ### Step 1. Setting .env

    ```bash=
    # Path : /

    # Backend env setting
    cp .env.sample .env
    vi .env

    Change required: SECRET_KEY,METADATA_SERVER_HOST,METADATA_SERVER_PORT
    ```

  - ### Step 2. Run Shell

    ```bash=
    # Path : /

    bash ./run_all.sh
    ```

- ## Q&A

  - Q: `docker compose up` container `aiml_file_mgt` run failed

    - A: `docker restart aiml_file_mgt` to restart the container

  - Q: `pip install` failed when `docker compose build`
    - A: `sudo apt update` and `sudo apt-get install python3-dev build-essential python3.8-dev python3.8-distutils libpython3.8-dev` to install the essential lib
