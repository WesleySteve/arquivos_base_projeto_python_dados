import os
from extract.collect import data_collect
from load.load import data_load


# definindo caminhos base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DIR = os.path.join(DATA_DIR, "raw")
BANCO_DIR = os.path.join(DATA_DIR, "base")


if __name__ == "__main__":

    # ELT

    # Collect
    data_raw, raw_dir = data_collect(RAW_DIR)

    if data_raw != []:

        # Load
        data_load(data_raw, raw_dir, banco_dir=BANCO_DIR)

        if data_load:

            print("Banco de dadsos criado com sucesso!")

        else:
            print("Erro ao criar o banco de dados!")

    else:
        print("Não existem arquivos para serem carregados!")
