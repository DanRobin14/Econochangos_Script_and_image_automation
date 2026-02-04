

# 'Main (Pendientes)'

# 'Llamar al master para definir el contexto del proyecto'
# 'Llamar al script generador para generar el guión de N lineas (Temporal)'
# 'Hacer loop for each (#linea,texto)'
# 'Función generar imagen(#linea,texto,context_image_generator)'
# 'Guardar imagenen en la carpeta de imagenes con el nombre en formato 001'
# 'Pedir miniatura usando el context_thumbnail'
# 'Guardar Thumbnail'

import time
t0_script = time.perf_counter()


# ' Definir cliente'

from dotenv import load_dotenv
load_dotenv()
from openai_client import get_client
import settings

client = get_client()
print("✅ OpenAI client inicializado.")
print("Model script:", settings.MODEL_SCRIPT)
print("Model image :", settings.MODEL_IMAGE)




# 'Leer ruta (Merged)'
from leer_ruta import get_caller_dir
ruta = get_caller_dir(__file__)
print(ruta)

# 'Crear folder de outputs y de context (Merged)'
from validar_carpeta import asegurar_carpeta_en_ruta
outputs_dir = asegurar_carpeta_en_ruta("outputs", ruta)
context_dir = asegurar_carpeta_en_ruta("context", ruta)
print(outputs_dir)
print(context_dir)


# 'Leer los txts context (Merged)'
from leer_context_files import leer_context_files
try:
    ctx = leer_context_files(ruta, carpeta_contexto="context", strict=True)
    print("✅ Context files cargados correctamente: master, script, image, thumbnail.")
except FileNotFoundError as e:
    print("❌ Error cargando context files:")
    print(e)
    raise
context_master = ctx.context_master
context_script_generator = ctx.context_script_generator
context_image_generator = ctx.context_image_generator
context_thumbnail_generator = ctx.context_thumbnail_generator
print(context_script_generator)


# 'Llamar al master para definir el contexto del proyecto'




# 'Definir el título y numero de lineas con variable de usuario (Merged)'
import argparse
def entero_positivo(value: str) -> int:
    try:
        n = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Debe ser un número entero (ej: 75).")
    if n <= 0:
        raise argparse.ArgumentTypeError("Debe ser un entero mayor a cero.")
    return n
parser = argparse.ArgumentParser(description="Generación de guion e imágenes - Econochangos")
parser.add_argument("--titulo", type=str, required=False, help="Título del guion")
parser.add_argument("--lineas", type=entero_positivo, required=False, help="Número de líneas del guion (entero > 0)")
args = parser.parse_args()

titulo = (args.titulo or "").strip()
if not titulo:
    titulo = input("Ingresa el título: ").strip()
if not titulo:
    raise ValueError("El título no puede estar vacío.")

lineas = args.lineas
while lineas is None:
    raw = input("Ingresa el número de líneas (entero > 0): ").strip()
    try:
        lineas = entero_positivo(raw)
    except argparse.ArgumentTypeError as e:
        print(f"Valor inválido: {e}")
        lineas = None
print("Título recibido:", titulo)
print("Número de líneas:", lineas)


# 'Llamar al script generador para generar el guión de N lineas (Temporal)'
from generar_guion import generar_guion
"""
response_str = generar_guion(
    client,
    model=settings.MODEL_SCRIPT,
    context_master=context_master,
    context_script_generator=context_script_generator,
    titulo=titulo,
    lineas=lineas,
    store=settings.OPENAI_STORE,
)
"""



# 'Tomar el output y guardarlo como txt (Merged)'
script_dir = ruta / "outputs"
script_file = script_dir / "script.txt"

from pathlib import Path

script_dir = ruta / "outputs"
script_file = script_dir / "script.txt"

response_str = script_file.read_text(encoding="utf-8-sig")  # o "utf-8" si no usas BOM
# script_file.write_text(response_str, encoding="utf-8-sig")

 

# 'Crear diccionario usando el output para definir pares (#linea,texto) (Merged)'
from segmentar_guion import segmentar_guion
chunks = segmentar_guion(response_str)


# 'Hacer loop for each (#linea,texto)'
# 'Función generar imagen(#linea,texto,context_image_generator)'
# 'Guardar imagenen en la carpeta de imagenes con el nombre en formato 001'

#from subir_referencias import subir_referencias
from generar_imagen import generar_imagen_con_refs
import settings
from pathlib import Path

# Subir referencias visuales (una sola vez)

from cache_refs import get_or_upload_reference_ids

refs_dir = ruta / "context" / "refs"
cache_path = ruta / "outputs" / "ref_cache.json"

ref_ids = get_or_upload_reference_ids(
    client,
    refs_dir=refs_dir,
    cache_path=cache_path,
    pattern="Estilo(*).*",
)
print(f"✅ Referencias listas: {len(ref_ids)}")





#images_dir = Path(outputs_dir) / settings.OUTPUTS_FOLDER_NAME

images_dir = Path(outputs_dir) / settings.OUTPUT_IMAGES_FOLDER_NAME
images_dir.mkdir(parents=True, exist_ok=True)


import time
from openai import BadRequestError

max_retries = 3
sleep_seconds = 1.5

for n in sorted(chunks):
    out_path = images_dir / f"{n:03d}.png"

    if out_path.exists():
        print(f"⏭️  Ya existe, skip: {out_path.name}")
        continue

    chunk_texto = chunks[n]  # incluye Texto + Visual

    ok = False
    last_err = None

    for attempt in range(1, max_retries + 1):
        t0_img = time.perf_counter()
        try:
            usage = generar_imagen_con_refs(
                client,
                model=settings.MODEL_SCRIPT,  # usa el modelo de texto que invoca tools
                context_image_generator=context_image_generator,
                chunk_texto=chunk_texto,
                ref_file_ids=ref_ids,
                out_path=out_path,
                size=settings.IMAGE_SIZE_SCENE,
                input_fidelity=settings.IMAGE_INPUT_FIDELITY,
            )

            t1_img = time.perf_counter()
            t1_script = time.perf_counter()
            print(f"✅ {out_path.name} generado en {t1_img - t0_img:.2f} s "
                  f"(total script: {t1_script - t0_script:.2f} s)")
            if usage:
                print(f"📊 Tokens {out_path.name}: {usage}")
            ok = True
            break

        except BadRequestError as e:
            last_err = e
            # Si es moderación, normalmente viene con "moderation_blocked"
            print(f"🚫 Error 400 en {out_path.name} (intento {attempt}/{max_retries}): {e}")
            if attempt < max_retries:
                time.sleep(sleep_seconds)

        except Exception as e:
            last_err = e
            print(f"❌ Error en {out_path.name} (intento {attempt}/{max_retries}): {e}")
            if attempt < max_retries:
                time.sleep(sleep_seconds)

    if not ok:
        print(f"❌ Se omitió {out_path.name} después de {max_retries} intentos. Último error: {last_err}")
        # continúas con el siguiente chunk
        continue









# 'Pedir miniatura usando el context_thumbnail'

# 'Guardar Thumbnail'


t1_script = time.perf_counter()
print(f"\n⏱️ Tiempo total del script: {t1_script - t0_script:.2f} s")
