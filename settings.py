'Definición de variables de entorno de OPEN AI'

# settings.py
from __future__ import annotations
from pathlib import Path

# --- OpenAI
OPENAI_STORE: bool = False  # no guardar por default

# Modelos (ajústalos luego si quieres)
MODEL_SCRIPT: str = "gpt-5"
MODEL_IMAGE: str = "gpt-image-1.5"

# Tamaños sugeridos (puedes cambiarlos luego)
IMAGE_SIZE_SCENE: str = "1024x1024"
IMAGE_SIZE_THUMB: str = "1024x1024"

# Calidad de fidelidad para generación de imágenes
IMAGE_INPUT_FIDELITY: str = "medium"

# Estructura de carpetas (relativa a la ruta base del proyecto)
OUTPUTS_FOLDER_NAME: str = "outputs"
OUTPUT_IMAGES_FOLDER_NAME: str = "images"
CONTEXT_FOLDER_NAME: str = "context"

# IMAGES_FOLDER_NAME: str = "images"  # dentro de outputs

# Referencias visuales (Feature 4; por ahora solo definido)
REFS_DIR: Path = Path("context")


REFS_DIR: Path = Path("context") / "refs"

REF_IMAGES = [
    str(p.as_posix())
    for p in sorted(REFS_DIR.glob("*"))
    if p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")
]

