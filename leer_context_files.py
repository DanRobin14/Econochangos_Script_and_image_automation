'Subrutina para leer los txt master y notificar si no se detecta alguno'

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class ContextFiles:
    context_master: str
    context_script_generator: str
    context_image_generator: str
    context_thumbnail_generator: str

    def as_dict(self) -> dict[str, str]:
        return {
            "context_master": self.context_master,
            "context_script_generator": self.context_script_generator,
            "context_image_generator": self.context_image_generator,
            "context_thumbnail_generator": self.context_thumbnail_generator,
        }


DEFAULT_FILES: tuple[str, ...] = (
    "context_master.txt",
    "context_script_generator.txt",
    "context_image_generator.txt",
    "context_thumbnail_generator.txt",
)


def _read_text_strict(path: Path, encoding: str = "utf-8-sig") -> str:
    """
    Lee texto. Si el archivo tiene BOM UTF-8, utf-8 lo maneja bien.
    Si esperas archivos con caracteres raros, puedes cambiar a 'utf-8-sig'.
    """
    return path.read_text(encoding=encoding)


def leer_context_files(
    ruta: str | Path,
    carpeta_contexto: str = "",   # por default, busca directo en `ruta`
    files: Iterable[str] = DEFAULT_FILES,
    strict: bool = True,
    encoding: str = "utf-8-sig",
) -> ContextFiles | tuple[ContextFiles | None, list[str]]:
    """
    Lee los context .txt y los almacena.

    Parameters
    ----------
    ruta : str | Path
        Ruta base (por ejemplo la carpeta del proyecto).
    carpeta_contexto : str
        Subcarpeta dentro de `ruta` donde están los .txt.
        Ej: "context" o "prompts/context". Si "", usa `ruta` directo.
    files : Iterable[str]
        Nombres de archivos a leer.
    strict : bool
        True -> si falta alguno lanza FileNotFoundError con detalle.
        False -> no lanza; devuelve (ContextFiles|None, missing_files)
    encoding : str
        Encoding usado al leer los archivos.

    Returns
    -------
    Si strict=True:
        ContextFiles
    Si strict=False:
        (ContextFiles|None, missing_files)
    """
    base = Path(ruta).expanduser().resolve()
    base = base / carpeta_contexto if carpeta_contexto else base

    files = tuple(files)
    missing = [f for f in files if not (base / f).is_file()]

    if missing:
        if strict:
            full_paths = "\n".join(str((base / f)) for f in missing)
            raise FileNotFoundError(
                "No se detectaron estos archivos de contexto:\n"
                f"{', '.join(missing)}\n\nRutas esperadas:\n{full_paths}"
            )
        return None, missing

    # Leer todos
    data: dict[str, str] = {}
    for fname in files:
        p = base / fname
        data[fname] = _read_text_strict(p, encoding=encoding)

    # Mapear a variables (campos del dataclass)
    ctx = ContextFiles(
        context_master=data["context_master.txt"],
        context_script_generator=data["context_script_generator.txt"],
        context_image_generator=data["context_image_generator.txt"],
        context_thumbnail_generator=data["context_thumbnail_generator.txt"],
    )

    return ctx if strict else (ctx, [])
