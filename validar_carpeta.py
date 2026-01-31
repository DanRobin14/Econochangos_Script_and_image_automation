'Subrutina para validar que la carpeta argumento esté creada en la carpeta argumento destino'

from pathlib import Path

def asegurar_carpeta_en_ruta(nombre_carpeta: str, ruta: str | Path) -> Path:

    if not isinstance(nombre_carpeta, str) or not nombre_carpeta.strip():
        raise ValueError("nombre_carpeta debe ser un string no vacío.")

    base = Path(ruta).expanduser().resolve()
    carpeta = base / nombre_carpeta

    carpeta.mkdir(parents=True, exist_ok=True)
    return carpeta
