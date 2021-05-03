# streamlit-conda-docker-nginx
Deployable and neatly structured streamlit project with reverse proxy. Docker-compose is used for managing containers. Works on Ubuntu

## Repository contents

- <code>/app</code> contains the main application code, the Dockerfile of the streamlit image as well as the conda environment file.
- <code>/app/src</code> is a directory for storing custom python modules used by the main application (app.py)
- <code>/nginx</code> contains everything related to nginx and its Dockerfile


## Instructions

**Make sure that you have docker-compose installed and working properly.**

1) Start by cd:ing into the repository root.

2) To build the images, run

```bash
sudo bash build.sh
```

3) To start the containers, run

```bash
sudo docker-compose up
```

4) To access the streamlit app, type the following into your web-browser:

```bash
localhost:80
```
