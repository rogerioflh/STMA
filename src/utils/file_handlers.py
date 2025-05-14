import os
import json

def ensure_dir_exists(filepath: str) -> None:
    """
    Garante que o diretório do caminho especificado exista.
    Cria o diretório, se necessário.
    """
    directory = os.path.dirname(filepath)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def read_json_file(filepath: str) -> dict | list:
    """
    Lê um arquivo JSON e retorna o conteúdo como dicionário ou lista.
    Retorna uma lista vazia se o arquivo estiver vazio ou não existir.
    """
    ensure_dir_exists(filepath)
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as e:
        print(f"[Erro ao ler JSON em '{filepath}']: {e}")
        return []
