

'Main'



'Leer ruta (Merged)'
from leer_ruta import get_caller_dir
ruta = get_caller_dir(__file__)
print(ruta)

'Crear folder de outputs y de context (Merged)'
from validar_carpeta import asegurar_carpeta_en_ruta
outputs_dir = asegurar_carpeta_en_ruta("outputs", ruta)
context_dir = asegurar_carpeta_en_ruta("context", ruta)
print(outputs_dir)
print(context_dir)


'Leer los txts context (Merged)'

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


'Llamar al master para definir el contexto del proyecto'




'Definir el título y numero de lineas con variable de usuario (Merged)'
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


'Llamar al script generador para generar el guión de N lineas (Temporal)'


response_str = """1.Línea: “Japón detonó una crisis de 20 trillones de dólares… y casi nadie lo vio venir.”
Visual:

Acción principal: Chango naranja señala una esfera gigante etiquetada “Japón” que vibra.

Elementos secundarios: Número enorme “20T” flotando como alarma.

Intención visual: Impacto inmediato y escala descomunal.

2.Línea: “Y lo peor: el golpe puede pegarle a tu portafolio en los próximos 90 días.”
Visual:

Acción principal: Chango mira un calendario con “90 días” marcado.

Elementos secundarios: Portafolio (carpeta) con señal de alerta.

Intención visual: Urgencia temporal clara.

3.Línea: “Porque Japón cruzó una línea que no se cruzaba desde hace 30 años.”
Visual:

Acción principal: Chango cruza una línea en el piso con letrero “30 años”.

Elementos secundarios: Huellas atrás, flecha hacia adelante.

Intención visual: Punto de no retorno.
"""


'Tomar el output y guardarlo como txt'
script_dir = ruta / "outputs"
script_file = script_dir / "script.txt"
script_file.write_text(response_str, encoding="utf-8-sig")

 



'Crear diccionario usando el output para definir pares (#linea,texto)'

'Hacer loop for each (#linea,texto)'

'Función generar imagen(#linea,texto,context_image_generator)'

'Guardar imagenen en la carpeta de imagenes con el nombre en formato 001'





'Pedir miniatura usando el context_thumbnail'

'Guardar Thumbnail'