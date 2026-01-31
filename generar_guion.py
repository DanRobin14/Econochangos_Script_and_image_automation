'Llamada a OPENAI para generar el guión apoyándonos del context master'

# generar_guion.py
from __future__ import annotations
from openai import OpenAI


def _extraer_texto_responses(resp) -> str:
    text = getattr(resp, "output_text", None)
    if isinstance(text, str) and text.strip():
        return text.strip()

    out = getattr(resp, "output", None)
    if isinstance(out, list):
        partes: list[str] = []
        for item in out:
            content = getattr(item, "content", None)
            if isinstance(content, list):
                for c in content:
                    if getattr(c, "type", None) in ("output_text", "text"):
                        t = getattr(c, "text", None)
                        if t:
                            partes.append(t)
        if partes:
            return "\n".join(partes).strip()

    return str(resp).strip()


def generar_guion(
    client: OpenAI,
    *,
    model: str,
    context_master: str,
    context_script_generator: str,
    titulo: str,
    lineas: int,
    store: bool = False,
) -> str:
    """
    Genera un guion usando Responses API.
    El formato y reglas ya vienen en context_master.
    """
    prompt_usuario = f"{context_script_generator}\nTítulo: {titulo}\nNúmero de líneas: {lineas}"

    resp = client.responses.create(
        model=model,
        instructions=context_master,
        input=prompt_usuario,
        store=store,
    )

    return _extraer_texto_responses(resp)
