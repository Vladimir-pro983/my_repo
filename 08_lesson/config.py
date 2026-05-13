"""Конфигурация для работы с Yougile API."""

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUGILE_API_KEY")
BASE_URL = "https://ru.yougile.com/api-v2"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
