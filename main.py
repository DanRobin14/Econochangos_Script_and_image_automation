

'Main'



'Leer ruta'
from leer_ruta import get_caller_dir
ruta = get_caller_dir(__file__)
print(ruta)

'Crear folder de outputs y de context'
from validar_carpeta import asegurar_carpeta_en_ruta
outputs_dir = asegurar_carpeta_en_ruta("outputs", ruta)
context_dir = asegurar_carpeta_en_ruta("context", ruta)
print(outputs_dir)
print(context_dir)


'Leer los txts context'

from leer_context_files import leer_context_files

try:
    ctx = leer_context_files(ruta, carpeta_contexto="context", strict=True)
    print("✅ Context files cargados correctamente: master, script, image, thumbnail.")
except FileNotFoundError as e:
    print("❌ Error cargando context files:")
    print(e)
    raise  # opcional: para cortar ejecución

# Variables listas para manipular
context_master = ctx.context_master
context_script_generator = ctx.context_script_generator
context_image_generator = ctx.context_image_generator
context_thumbnail_generator = ctx.context_thumbnail_generator




'Llamar al master para definir el contexto del proyecto'

'Definir el título con variable de usuario'

'Definir el número de lineas con variable de usuario'

'Llamar al script generador para generar el guión de N lineas'

'Tomar el output y guardarlo como txt'

'Crear diccionario usando el output para definir pares (#linea,texto)'

'Hacer loop for each (#linea,texto)'

'Función generar imagen(#linea,texto,context_image_generator)'

'Guardar imagenen en la carpeta de imagenes con el nombre en formato 001'

'Pedir miniatura usando el context_thumbnail'

'Guardar Thumbnail'