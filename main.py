

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


response_str = """**🚨 ¡ALERTA! TU BANCO NO QUIERE QUE SEPAS ESTO**

1.Línea: “Alerta Econochangos.”
Visual:
Chango naranja serio levantando una señal roja de alerta.

2.Línea: “Febrero de 2026 cambió las reglas del juego.”
Visual:
Calendario marcando “Feb 2026” con signo de advertencia.

3.Línea: “Los bancos no lo anunciaron.”
Visual:
Chango corporativo gris escondiendo un documento.

4.Línea: “Pero ya está confirmado.”
Visual:
Sello grande que dice “CONFIRMADO”.

5.Línea: “Hay normas que esconden en la letra chiquita.”
Visual:
Contrato enorme con lupa enfocando texto pequeño.

6.Línea: “Y tú pagas comisiones sin saberlo.”
Visual:
Bananas saliendo del bolsillo del chango.

7.Línea: “Hoy te voy a explicar lo que no te dicen.”
Visual:
Chango naranja señalando al espectador.

8.Línea: “Son 7 realidades bancarias.”
Visual:
Número “7” grande con iconos alrededor.

9.Línea: “Y todas afectan tu dinero.”
Visual:
Banana agrietándose.

10.Línea: “Empezamos fuerte.”
Visual:
Chango golpeando una mesa.

---

11.Línea: “Primera realidad: el banco NO es tu amigo.”
Visual:
Chango naranja frente a chango corporativo gris.

12.Línea: “Su negocio es cobrarte.”
Visual:
Caja registradora con bananas.

13.Línea: “Aunque tú creas que ‘no pasa nada’.”
Visual:
Chango confiado mirando su app.

14.Línea: “Cada comisión suma.”
Visual:
Contador subiendo lentamente.

15.Línea: “Y a largo plazo duele.”
Visual:
Montón de bananas reducido.

---

16.Línea: “Segunda realidad: existe la cuenta gratuita por ley.”
Visual:
Documento con título “Cuenta básica”.

17.Línea: “Sí, gratuita.”
Visual:
Texto grande: “$0”.

18.Línea: “Está en el Artículo 48 Bis 2.”
Visual:
Artículo legal resaltado.

19.Línea: “Pero casi nadie la pide.”
Visual:
Chango confundido rascándose la cabeza.

20.Línea: “Porque el banco no te la ofrece.”
Visual:
Empleado bancario mirando hacia otro lado.

21.Línea: “Tienes que exigirla.”
Visual:
Chango firme señalando el mostrador.

---

22.Línea: “Tercera realidad: el saldo promedio diario.”
Visual:
Gráfica diaria subiendo y bajando.

23.Línea: “No es tu saldo final.”
Visual:
Dos números distintos comparándose.

24.Línea: “Es el promedio de todo el mes.”
Visual:
Calendario con sumas diarias.

25.Línea: “Un solo error te cobra comisión.”
Visual:
Un día marcado en rojo.

26.Línea: “Aunque cierres bien el mes.”
Visual:
Chango sorprendido viendo el estado de cuenta.

---

27.Línea: “Cuarta realidad: el pago mínimo.”
Visual:
Tarjeta con texto “Pago mínimo”.

28.Línea: “Parece ayuda.”
Visual:
Mano extendida.

29.Línea: “Pero es una trampa.”
Visual:
Trampa cerrándose sobre bananas.

30.Línea: “Pagas intereses eternos.”
Visual:
Reloj sin fin girando.

31.Línea: “Y tu deuda casi no baja.”
Visual:
Saldo disminuyendo apenas.

---

32.Línea: “Quinta realidad: comisiones ocultas en fondos.”
Visual:
Fondo de inversión con etiquetas escondidas.

33.Línea: “No todo es rendimiento.”
Visual:
Gráfica con mordidas.

34.Línea: “Hay cargos por manejo.”
Visual:
Bananas siendo cortadas.

35.Línea: “Cargos por entrada.”
Visual:
Puerta cobrando peaje.

36.Línea: “Y cargos por salida.”
Visual:
Puerta de salida con símbolo de costo.

---

37.Línea: “Sexta realidad: adelantar a capital.”
Visual:
Chango con calculadora.

38.Línea: “No es pagar de más.”
Visual:
Banana regresando al montón.

39.Línea: “Es pagar mejor.”
Visual:
Deuda encogiéndose rápido.

40.Línea: “Pero debe ir etiquetado correctamente.”
Visual:
Etiqueta que dice “Capital”.

41.Línea: “Si no, el banco gana.”
Visual:
Chango corporativo sonriendo.

---

42.Línea: “Séptima realidad: el efectivo es peligroso.”
Visual:
Billetes con señal de alerta.

43.Línea: “Retirar de tu tarjeta deja rastro.”
Visual:
Huella marcada sobre dinero.

44.Línea: “Y cuesta caro.”
Visual:
Bananas cayendo por un agujero.

45.Línea: “Más de lo que crees.”
Visual:
Número grande con signo de advertencia.

---

46.Línea: “Ahora hablemos del SAT.”
Visual:
Radar girando.

47.Línea: “Tus cuentas son un radar automático.”
Visual:
Cuentas bancarias conectadas al radar.

48.Línea: “No importa si es tu dinero.”
Visual:
Chango levantando su banana.

49.Línea: “Importa cómo se mueve.”
Visual:
Flechas entre cuentas.

50.Línea: “Traspasos mal etiquetados levantan alertas.”
Visual:
Alarma roja sobre transferencia.

---

51.Línea: “No es ilegal.”
Visual:
Sello “Legal”.

52.Línea: “Pero sí sospechoso.”
Visual:
Ojo observando al chango.

53.Línea: “Y eso dispara revisiones.”
Visual:
Lupa gigante.

54.Línea: “Evítalas con orden.”
Visual:
Cajones bien acomodados.

---

55.Línea: “La mayoría nunca revisa esto.”
Visual:
Changos dormidos.

56.Línea: “Por eso pierden dinero.”
Visual:
Bananas escapando.

57.Línea: “No porque sean tontos.”
Visual:
Chango serio.

58.Línea: “Sino porque nadie se los explica.”
Visual:
Libro cerrado.

---

59.Línea: “Ahora tú ya lo sabes.”
Visual:
Libro abierto frente al chango.

60.Línea: “Y el conocimiento protege.”
Visual:
Escudo frente a bananas.

61.Línea: “Más que cualquier banco.”
Visual:
Escudo más grande que el banco.

---

62.Línea: “Revisa tus contratos.”
Visual:
Chango leyendo documentos.

63.Línea: “Exige la cuenta gratuita.”
Visual:
Chango levantando un formulario.

64.Línea: “Cuida tu saldo promedio.”
Visual:
Calendario controlado.

65.Línea: “Evita el pago mínimo.”
Visual:
Tarjeta siendo tachada.

66.Línea: “Invierte con comisiones claras.”
Visual:
Gráfica limpia y simple.

67.Línea: “Etiqueta bien tus traspasos.”
Visual:
Transferencia con etiqueta correcta.

---

68.Línea: “Esto no es paranoia.”
Visual:
Chango tranquilo.

69.Línea: “Es educación financiera.”
Visual:
Banana sólida con etiqueta “Conocimiento”.

70.Línea: “Y te da poder.”
Visual:
Chango firme y erguido.

---

71.Línea: “Los bancos cuentan con que no preguntes.”
Visual:
Empleado bancario confiado.

72.Línea: “Ahora sí lo harás.”
Visual:
Chango levantando la mano.

73.Línea: “Porque tu dinero es tuyo.”
Visual:
Chango abrazando sus bananas.

74.Línea: “Y debe trabajar para ti.”
Visual:
Bananas creciendo.

75.Línea: “Econochangos: piensa antes de morder la banana.”
Visual:
Fondo blanco. Chango naranja reflexivo con banana intacta.

"""


'Tomar el output y guardarlo como txt'
script_dir = ruta / "outputs"
script_file = script_dir / "script.txt"
script_file.write_text(response_str, encoding="utf-8-sig")

 

'Crear diccionario usando el output para definir pares (#linea,texto)'
from segmentar_guion import segmentar_guion
chunks = segmentar_guion(response_str)

for n in sorted(chunks):
    print("----", n, "----")
    print(chunks[n])



'Hacer loop for each (#linea,texto)'

'Función generar imagen(#linea,texto,context_image_generator)'

'Guardar imagenen en la carpeta de imagenes con el nombre en formato 001'





'Pedir miniatura usando el context_thumbnail'

'Guardar Thumbnail'