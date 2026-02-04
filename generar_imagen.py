'Rutina para generar imágenes a partir del texto del chunk.'

# generar_imagen.py
from __future__ import annotations

import base64
from pathlib import Path
from typing import Any, Dict, Optional
from openai import OpenAI


def _extraer_b64_imagen(resp: Any) -> str:
    """
    Busca el resultado base64 de la llamada a image_generation dentro de resp.output.
    Compatible con variaciones del SDK.
    """
    output = getattr(resp, "output", None)

    # Caso típico: resp.output es lista de objetos con .type
    if isinstance(output, list):
        for item in output:
            t = getattr(item, "type", None)
            if t == "image_generation_call":
                b64 = getattr(item, "result", None)
                if isinstance(b64, str) and b64.strip():
                    return b64

    # Fallback defensivo
    raise RuntimeError("No se pudo extraer la imagen (base64) de la respuesta.")


def _extraer_usage_tokens(resp: Any) -> Optional[Dict[str, int]]:
    """
    Extrae el desglose de tokens si está disponible en la respuesta.
    """
    usage = getattr(resp, "usage", None)
    if usage is None:
        return None

    tokens: Dict[str, int] = {}
    for key in ("input_tokens", "output_tokens", "total_tokens"):
        value = getattr(usage, key, None)
        if isinstance(value, int):
            tokens[key] = value

    return tokens or None


def generar_imagen_con_refs(
    client: OpenAI,
    *,
    model: str,
    context_image_generator: str,
    chunk_texto: str,
    ref_file_ids: list[str],
    out_path: Path,
    size: str = "1536x1024",
    input_fidelity: str = "high",
) -> Optional[Dict[str, int]]:
    """
    Genera una imagen PNG para un chunk usando referencias visuales (file_id).
    """
    prompt = (
        f"{context_image_generator}\n\n"
        f"Ahora genera una imagen para esta linea:\n\n"
        f"{chunk_texto}\n\n"
        f"Reglas extra:\n"
        f"- Fondo blanco\n"
        f"- Sin texto en la imagen salvo que la escena lo pida explícitamente\n"
        f"- Mantén proporciones y estilo idénticos a las referencias\n"
    )

    resp = client.responses.create(
        model=model,
        input=[{
            "role": "user",
            "content": (
                [{"type": "input_text", "text": prompt}]
                + [{"type": "input_image", "file_id": fid} for fid in ref_file_ids]
            ),
        }],
        tools=[{
            "type": "image_generation",
            "action": "generate",
            "input_fidelity": input_fidelity,
            "size": size,
        }],
        store=False,
    )

    b64 = _extraer_b64_imagen(resp)
    img_bytes = base64.b64decode(b64)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(img_bytes)

    return _extraer_usage_tokens(resp)
