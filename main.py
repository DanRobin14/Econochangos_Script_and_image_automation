

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