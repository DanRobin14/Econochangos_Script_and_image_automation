'Subrutina para definir directorio desde donde corre el programa'

from pathlib import Path

def get_caller_dir(caller_file: str | Path) -> Path:
    """
    Devuelve la carpeta (Path absoluto) donde vive el archivo que invoca la subrutina.
    Uso recomendado: pásale __file__ desde el script principal.
    """
    caller_path = Path(caller_file).expanduser().resolve()
    return caller_path.parent