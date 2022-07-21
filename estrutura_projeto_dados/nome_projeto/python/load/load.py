import os

import pandas as pd

from bancoslib.db.sqlite import create_db_sqlite


def data_load(data_raw, raw_dir, banco_dir=None):
    """Função responsavel em carregar os dados no banco de dados"""

    nome_banco = str(input("Digite o nome do banco de dados: "))

    if banco_dir == None:

        con = create_db_sqlite(raw_dir, nome_banco)

    con = create_db_sqlite(banco_dir, nome_banco)

    if con:

        for i in data_raw:
            df_tmp = pd.read_csv(os.path.join(raw_dir, i))
            # coloque a funcao abaixo na frente do ) caso queira remover
            # alguma parte no nome do arquivo
            # ex: .replace("olist_", "")
            nome_tabela = i.strip(".csv")
            df_tmp.to_sql(nome_tabela, con, if_exists="replace", index=False)

        return True

    return False
