'Definición de variables de entorno de OPEN AI'

# settings.py
from __future__ import annotations
from pathlib import Path

# --- OpenAI
OPENAI_STORE: bool = False  # no guardar por default

# Modelos (ajústalos luego si quieres)
MODEL_SCRIPT: str = "gpt-5"
MODEL_IMAGE: str = "gpt-image-1"

# Tamaños sugeridos (puedes cambiarlos luego)
IMAGE_SIZE_SCENE: str = "1536x1024"
IMAGE_SIZE_THUMB: str = "1536x1024"

# Estructura de carpetas (relativa a la ruta base del proyecto)
OUTPUTS_FOLDER_NAME: str = "outputs"
CONTEXT_FOLDER_NAME: str = "context"

# IMAGES_FOLDER_NAME: str = "images"  # dentro de outputs

# Referencias visuales (Feature 4; por ahora solo definido)
REFS_DIR: Path = Path("context")
REF_IMAGES: list[str] = [
    str(REFS_DIR / "Estilo(1).jpeg"),
    str(REFS_DIR / "Estilo(2).jpeg"),
]
