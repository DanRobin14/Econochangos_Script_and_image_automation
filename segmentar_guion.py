'Subrutina para segmentar el guión que arroje open ai y crear un diccionario con pares (número de linea, texto)'

# segmentar_guion.py
import re
from typing import Dict

_LINE_BLOCK_RE = re.compile(
    r'(?ms)^\s*(\d+)\s*\.\s*L[íi]nea\s*:\s*(.*?)\s*(?=^\s*\d+\s*\.\s*L[íi]nea\s*:|\Z)'
)

def segmentar_guion(response_str: str) -> Dict[int, str]:
    """
    Retorna dict {numero_linea: bloque_texto} tomando bloques que empiezan con:
    N.Línea: ...
    """
    out: Dict[int, str] = {}
    for m in _LINE_BLOCK_RE.finditer(response_str):
        n = int(m.group(1))
        bloque = m.group(2).strip()
        out[n] = bloque
    return out
