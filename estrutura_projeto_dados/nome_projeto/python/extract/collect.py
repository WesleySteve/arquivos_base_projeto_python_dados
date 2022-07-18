import os


def data_collect(path=None):
    """Collect de dados

    - defina os diretórios listados abaixo em seu projeto
        antes de chamar esta função

    - esta variavel identifica o diretório raiz do proje
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))))

    - esta variavel identifica o diretório dos dados
    DATA_DIR = os.path.join(BASE_DIR, "data")

    - esta variavel identifica o diretório dos dados brutos baixados (.csv)
    RAW_DIR = os.path.join(DATA_DIR, "raw")

    - esta variavel identifica o diretório de onde ficará armazenado o
        banco de dados sqlite (.db)
    BANCO_DIR = os.path.join(DATA_DIR, "base")

    """

    if path != "":

        nomes_arquivos = [i for i in os.listdir(path) if i.endswith(".csv")]
        if nomes_arquivos != "":
            return nomes_arquivos, path

    return None
