'Subrutina para subir las referencias y reutilizarlas en caso de ya haberlas subido'

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

from openai import OpenAI


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    """
    Hash SHA-256 del contenido del archivo (estable, independiente del nombre/fecha).
    """
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def listar_refs(refs_dir: Path, pattern: str = "Estilo(*).jpeg") -> List[Path]:
    """
    Lista archivos de refs en orden determinista.
    Ajusta pattern si tienes .jpg/.png mezclados.
    """
    files = sorted(refs_dir.glob(pattern))
    # También podrías incluir jpg/png automáticamente:
    # files = sorted(set(refs_dir.glob("*.jpg")) | set(refs_dir.glob("*.jpeg")) | set(refs_dir.glob("*.png")))
    return files


def _load_cache(cache_path: Path) -> Dict[str, Dict]:
    if not cache_path.exists():
        return {}
    try:
        return json.loads(cache_path.read_text(encoding="utf-8"))
    except Exception:
        # si se corrompió, lo reiniciamos
        return {}


def _save_cache(cache_path: Path, data: Dict[str, Dict]) -> None:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


@dataclass
class RefInfo:
    filename: str
    sha256: str
    file_id: str
    abs_path: Path


def get_or_upload_reference_ids(
    client: OpenAI,
    *,
    refs_dir: Path,
    cache_path: Path,
    pattern: str = "Estilo(*).*",
    purpose: str = "vision",
) -> List[str]:
    """
    Devuelve file_ids para TODAS las refs en refs_dir.
    Reusa file_ids desde cache si el SHA256 coincide; sube solo lo nuevo/cambiado.
    """
    refs = listar_refs(refs_dir, pattern=pattern)
    if not refs:
        raise FileNotFoundError(f"No se encontraron referencias en: {refs_dir} con pattern={pattern}")

    cache = _load_cache(cache_path)

    resolved: List[RefInfo] = []
    changed = False

    for p in refs:
        digest = sha256_file(p)
        key = digest  # clave por contenido; si renombraste archivo, igual reusa

        if key in cache and "file_id" in cache[key]:
            file_id = cache[key]["file_id"]
        else:
            # Subir solo si no existe en cache
            with open(p, "rb") as f:
                up = client.files.create(file=f, purpose=purpose)
            file_id = up.id

            cache[key] = {
                "file_id": file_id,
                "sha256": digest,
                "filename": p.name,
            }
            changed = True

        resolved.append(RefInfo(filename=p.name, sha256=digest, file_id=file_id, abs_path=p.resolve()))

    if changed:
        _save_cache(cache_path, cache)

    # Mantén orden estable igual a archivos (Estilo(1)...Estilo(10))
    return [r.file_id for r in resolved]
