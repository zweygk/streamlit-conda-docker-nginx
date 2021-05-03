FROM continuumio/miniconda3

RUN conda update conda

COPY ./environment.yml /environment.yml
WORKDIR /

RUN conda env create -f ./environment.yml
RUN rm -rf /environment.yml

ENV PATH /opt/conda/envs/streamlit-app-env/bin:$PATH
ENV CONDA_DEFAULT_ENV streamlit-app-env
ENV CONDA_PREFIX /opt/conda/envs/streamlit-app-env

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN mkdir -p /.streamlit

RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
" > /.streamlit/config.toml'

EXPOSE 8501

