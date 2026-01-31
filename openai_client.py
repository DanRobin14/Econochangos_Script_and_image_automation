'Subrutina para definir el entorno de open AI, la API key y esas cosas'

# openai_client.py
from __future__ import annotations

import os
from openai import OpenAI


def get_client() -> OpenAI:
    """
    Crea un cliente OpenAI leyendo OPENAI_API_KEY del entorno.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or not api_key.strip():
        raise EnvironmentError(
            "Falta OPENAI_API_KEY en variables de entorno. "
            "Configúrala antes de ejecutar el script."
        )
    return OpenAI(api_key=api_key)
