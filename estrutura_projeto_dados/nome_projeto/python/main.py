from extract.collect import data_collect
from load.load import data_load


if __name__ == "__main__":

    # ELT

    # Collect
    data_raw, raw_dir = data_collect()

    if data_raw != []:

        # Load
        data_load(data_raw, raw_dir, banco_dir=None)

        if data_load:

            print("Banco de dadsos criado com sucesso!")

        else:
            print("Erro ao criar o banco de dados!")

    else:
        print("Não existem arquivos para serem carregados!")
