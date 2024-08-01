## BASE IMAGE
FROM jupyter/minimal-notebook
ARG env_name=CDCBRFSS

## SET WORKING DIRECTORY
WORKDIR /app

## CREATE CONDA ENVIRONMENT
RUN conda update conda \
    && conda create --name $env_name


## MAKE ALL BELOW RUN COMMANDS USE THE NEW CONDA ENVIRONMENT
RUN echo "conda activate $env_name" >> ~/.bashrc
RUN conda install html5lib pandas numpy psycopg2
RUN conda run -n $env_name python -m ipykernel install --user --name=$env_name

## COPY REST OF THE FILES
COPY . .

## Run Jupyter Notebook
CMD ["jupyter", "notebook", "--port=8889", "--no-browser", "--ip=0.0.0.0", "--allow-root"]

