'Script para subir los changos que hay en context y conservar el estilo de dibujo econochangos.'

# subir_referencias.py
from __future__ import annotations

from pathlib import Path
from openai import OpenAI


def subir_referencias(
    client: OpenAI,
    *,
    base_dir: Path,
    ref_paths: list[str],
) -> list[str]:
    """
    Sube imágenes de referencia (paths relativos) y devuelve lista de file_id.
    """
    file_ids: list[str] = []

    for p in ref_paths:
        path = (base_dir / p).resolve()
        if not path.exists():
            raise FileNotFoundError(f"No existe referencia: {path}")

        with open(path, "rb") as f:
            uploaded = client.files.create(
                file=f,
                purpose="vision",  # requerido para poder usarla como input_image
            )
        file_ids.append(uploaded.id)

    return file_ids
