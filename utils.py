import json
from app.config import BaseConfig


def read_data_from_json() -> dict:
    """Чтение данных из json-файла"""
    with open(BaseConfig.DATA_DIR, encoding="UTF-8") as f:
        data = json.load(f)
    return data
