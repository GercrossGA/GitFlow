# Chatbot para venta de zapatos
import random

# Catálogo de zapatos (simulado)
catalogo_zapatos = [
    {"id": 1, "nombre": "Zapatos Deportivos", "precio": 59.99, "tallas": [38, 39, 40, 41, 42, 43], "colores": ["negro", "blanco", "rojo"]},
    {"id": 2, "nombre": "Botas de Montaña", "precio": 89.99, "tallas": [39, 40, 41, 42, 43, 44], "colores": ["marrón", "negro"]},
    {"id": 3, "nombre": "Zapatos de Vestir", "precio": 79.99, "tallas": [38, 39, 40, 41, 42], "colores": ["negro", "azul"]},
    {"id": 4, "nombre": "Sandalias Playa", "precio": 29.99, "tallas": [36, 37, 38, 39, 40, 41, 42], "colores": ["azul", "rojo", "verde"]},
    {"id": 5, "nombre": "Zapatos Casuales", "precio": 49.99, "tallas": [37, 38, 39, 40, 41, 42, 43], "colores": ["negro", "gris", "blanco"]}
]

# Respuestas predefinidas 
respuestas = {
    "saludo": [
        "¡Hola! Bienvenido a la mejor tienda de zapatos de la ciudad. ¿En qué puedo ayudarte hoy?", 
        "¡Qué gusto verte por aquí! Soy tu asistente para encontrar el calzado perfecto. ¿Qué estás buscando?", 
        "¡Hola! Encantado de atenderte. ¿Qué tipo de zapatos te interesan hoy?"
    ],
    "despedida": [
        "¡Hasta pronto! Espero verte nuevamente por aquí. ¡Que tengas un excelente día!", 
        "¡Gracias por visitarnos! Si necesitas más ayuda, no dudes en volver. ¡Cuídate mucho!", 
        "¡Ha sido un placer ayudarte! Vuelve pronto y encuentra los zapatos de tus sueños. ¡Hasta la próxima! "
    ],
    "agradecimiento": [
        "¡De nada! Estoy aquí para hacer tu experiencia de compra más agradable. ¿Hay algo más en lo que pueda ayudarte?", 
        "¡Es un placer ayudarte! Si tienes más preguntas, no dudes en hacerlas. ¡Estoy a tu disposición!"
    ],
    "no_entiendo": [
        "Disculpa, no he entendido bien lo que buscas. ¿Podrías explicármelo de otra forma?", 
        "Disculpa, no estoy seguro de haber entendido tu pregunta. ¿Podrías reformularla?", 
        "Lo siento, parece que no he comprendido bien. ¿Me explicas nuevamente lo que necesitas? ¡Gracias por tu paciencia!"
    ],
    "ver_catalogo": [
        "¡Claro! Tenemos una variedad de colección que incluye: Zapatos Deportivos, Botas de Montaña, Zapatos de Vestir, Sandalias de Playa y Zapatos Casuales.",

    ],
    "tallas_disponibles": [
        "Contamos con un amplio rango de tallas, generalmente desde la 36 hasta la 44, dependiendo del modelo.",  
    ],
     "devoluciones": [
        "En cuanto a devoluciones, te ofrecemos 20 días para devolver o cambiar tus zapatos. Los productos deben estar sin usar y en su caja original."
    ],
    "cambios_talla": [
        "¡Claro que puedes cambiar la talla! puedes solicitar un cambio de talla dentro de los 20 días posteriores a la compra, siempre que estén sin usar y con su empaque original."
    ],
}

def buscar_zapatos(tipo):
    resultados = []
    tipo = tipo.lower()
    
    for zapato in catalogo_zapatos:
        nombre_lower = zapato['nombre'].lower()
        if tipo in nombre_lower:
            resultados.append(zapato)
    
    if resultados:
        respuesta = "¡Genial! He encontrado estos modelos para ti:\n"
        for zapato in resultados:
            respuesta += f"- {zapato['nombre']}: ${zapato['precio']} (Tallas: {', '.join(map(str, zapato['tallas']))}, Colores: {', '.join(zapato['colores'])})\n"
        respuesta += "\n¿Te gustaría conocer más detalles sobre alguno de estos modelos? "
        return respuesta
    else:
        return f"Lo siento, parece que no tenemos zapatos del tipo '{tipo}' en este momento. ¿Te gustaría ver otros estilos de zapatos? "

def verificar_talla(talla, modelo=None):
    try:
        talla = int(talla)
        
        if modelo:
            # Buscar modelo específico
            modelo = modelo.lower()
            for zapato in catalogo_zapatos:
                if modelo in zapato['nombre'].lower():
                    if talla in zapato['tallas']:
                        return f"¡Buenas noticias! Sí tenemos disponible la talla {talla} para {zapato['nombre']} en los colores: {', '.join(zapato['colores'])}. ¿Te interesa algún color en particular?"
                    else:
                        tallas_cercanas = [t for t in zapato['tallas'] if abs(t - talla) <= 1]
                        if tallas_cercanas:
                            return f"Lo siento, no tenemos la talla {talla} para {zapato['nombre']}. Pero tenemos tallas cercanas: {', '.join(map(str, tallas_cercanas))}. ¿Te gustaría probar alguna de estas?"
                        else:
                            return f"Lo siento, no tenemos la talla {talla} para {zapato['nombre']} ni tallas cercanas. ¿Te gustaría ver otros modelos similares?"
            
            return f"No he podido encontrar el modelo '{modelo}' en nuestro catálogo. ¿Podrías ser más específico o quieres ver todos nuestros modelos disponibles?"
        else:
            # Verificar en todos los modelos
            modelos_disponibles = []
            for zapato in catalogo_zapatos:
                if talla in zapato['tallas']:
                    modelos_disponibles.append(zapato['nombre'])
            
            if modelos_disponibles:
                return f"¡Excelente! Tenemos la talla {talla} disponible en los siguientes modelos: {', '.join(modelos_disponibles)}. ¿Cuál de estos te interesa más?"
            else:
                return f"Lo siento, actualmente no tenemos la talla {talla} en ninguno de nuestros modelos. ¿Te gustaría que te muestre las tallas disponibles más cercanas?"
    except ValueError:
        return "Por favor, ingresa un número válido para la talla. Por ejemplo: 38, 39, 40, etc. Solo manejamos numeros enteros"

def recomendar_por_ocasion(ocasion):
    ocasion = ocasion.lower()
    if "deporte" in ocasion or "correr" in ocasion or "entrenar" in ocasion:
        return "Para actividades deportivas, te recomiendo nuestros Zapatos Deportivos. Son ligeros, cómodos y tienen excelente soporte para tus pies durante el ejercicio. ¿Te gustaría ver los colores y tallas disponibles?"
    elif "formal" in ocasion or "trabajo" in ocasion or "oficina" in ocasion or "vestir" in ocasion:
        return "Para ocasiones formales, nuestros Zapatos de Vestir son la opción perfecta. Son elegantes, cómodos para uso diario y vienen en colores clásicos que combinan con todo. ¿Te interesa conocer más detalles?"
    elif "casual" in ocasion or "diario" in ocasion or "día a día" in ocasion:
        return "Para uso diario, los Zapatos Casuales son ideales. Combinan estilo y comodidad para tus actividades del día a día. ¿Quieres que te cuente más sobre estos modelos?"
    elif "playa" in ocasion or "piscina" in ocasion or "verano" in ocasion:
        return "Para disfrutar del verano, las Sandalias de Playa son perfectas. Son frescas, resistentes al agua y vienen en colores vibrantes. ¿Te gustaría conocer las tallas disponibles?"
    elif "montaña" in ocasion or "senderismo" in ocasion or "campo" in ocasion:
        return "Para aventuras al aire libre, nuestras Botas de Montaña ofrecen excelente soporte y tracción. Son impermeables y muy duraderas. ¿Te interesa saber más sobre ellas?"
    else:
        return "No estoy seguro para qué ocasión buscas zapatos. ¿Podrías darme más detalles? Tenemos opciones para actividades deportivas, uso casual, ocasiones formales, playa y montaña."

def get_response(mensaje):
    mensaje = mensaje.lower()
    
    # Saludos
    if any(palabra in mensaje for palabra in ["hola", "buenos dias", "buenas tardes", "buenas noches", "buenas", "saludos"]):
        return random.choice(respuestas["saludo"])
    
    # Despedidas
    elif any(palabra in mensaje for palabra in ["adios", "hasta luego", "bye", "nos vemos"]):
        return random.choice(respuestas["despedida"])
    
    # Agradecimientos
    elif any(palabra in mensaje for palabra in ["gracias", "te lo agradezco", "muchas gracias"]):
        return random.choice(respuestas["agradecimiento"])
    
    # Ver catálogo
    elif any(frase in mensaje for frase in ["que zapatos tienen", "mostrar catalogo", "busco zapatos", "modelos", "modelos disponibles", "muestrame", "necesito zapatos"]):
        return random.choice(respuestas["ver_catalogo"])
    
    # Verificar tallas (general)
    elif any(frase in mensaje for frase in ["tallas disponibles", "que tallas", "hay en talla"]):
        return random.choice(respuestas["tallas_disponibles"])
    
    # Verificar talla específica en modelo específico
    elif "talla" in mensaje and any(zapato['nombre'].lower() in mensaje.lower() for zapato in catalogo_zapatos):
        # Extraer talla mencionada
        palabras = mensaje.split()
        talla = None
        modelo = None
        
        # Buscar un número en el mensaje
        for palabra in palabras:
            if palabra.isdigit() and 30 < int(palabra) < 50:  # Rango razonable de tallas
                talla = palabra
                break
        
        # Identificar el modelo
        for zapato in catalogo_zapatos:
            if zapato['nombre'].lower() in mensaje.lower():
                modelo = zapato['nombre']
                break
        
        if talla and modelo:
            return verificar_talla(talla, modelo)
        elif talla:
            return verificar_talla(talla)
        elif modelo:
            return f"¿Qué talla estás buscando para los {modelo}? Puedo verificar la disponibilidad por ti."
        else:
            return "¿Podrías indicarme qué talla y qué modelo te interesan? Así podré verificar la disponibilidad específica."
    
    # Verificar solo talla específica
    elif "talla" in mensaje and any(palabra.isdigit() and 30 < int(palabra) < 50 for palabra in mensaje.split()):
        # Extraer talla mencionada
        for palabra in mensaje.split():
            if palabra.isdigit() and 30 < int(palabra) < 50:
                return verificar_talla(palabra)
    
    # Recomendación por la ocacion o el uso 
    elif "para" in mensaje and any(palabra in mensaje for palabra in ["ocasion", "usar", "utilizarlos", "evento", "actividad"]):
        # Extraer la ocasión
        ocasion = mensaje.split("para")[1].strip()
        return recomendar_por_ocasion(ocasion)
    
    # Buscar zapatos específicos
    elif "deportivos" in mensaje or "correr" in mensaje:
        return buscar_zapatos("deportivos")
    elif "botas" in mensaje or "montaña" in mensaje:
        return buscar_zapatos("botas")
    elif "vestir" in mensaje:
        return buscar_zapatos("vestir")
    elif "sandalias" in mensaje or "playa" in mensaje:
        return buscar_zapatos("sandalias")
    elif "casuales" in mensaje or "zapatillas" in mensaje:
        return buscar_zapatos("casuales")
    
    # Información de envío
    elif any(palabra in mensaje for palabra in ["envio", "envios", "entrega","cuando llega"]):
        return "Los envíos nacionales tardan entre 3-5 días hábiles, mientras que los internacionales toman de 10 a 15 días."
    
    # Descuentos
    elif any(palabra in mensaje for palabra in ["descuento", "oferta", "promocion", "rebaja", "barato"]):
        return "¡Tenemos ofertas increíbles para ti! Actualmente ofrecemos un 20% de descuento en todos nuestros zapatos deportivos y un 15% en compras superiores a $100. ¿Te gustaría aprovechar alguna de estas promociones?"
    
    #devoluciones
    elif any(palabra in mensaje for palabra in ["devolucion", "devoluciones", "devolver"]):
        return random.choice(respuestas["devoluciones"])

    #cambio de talla
    elif "cambio" in mensaje and "talla" in mensaje:
        return random.choice(respuestas["cambios_talla"])

    # Respuesta por defecto
    else:
        return random.choice(respuestas["no_entiendo"])

# Función principal
def main():
    print("-----¡Bienvenido a ZapatosBot!------")
    print("Soy tu asistente virtual para ayudarte a encontrar los zapatos perfectos.")
    print("Escribe 'salir' para terminar la conversación.")
    
    while True:
        mensaje_usuario = input("¿En qué puedo ayudarte?: ")
        
        if mensaje_usuario.lower() == 'salir':
            print("ZapatosBot: ¡Gracias por visitarnos! Ha sido un placer atenderte. ¡Que tengas un día maravilloso!")
            break
        
        respuesta = get_response(mensaje_usuario)
        print(f"ZapatosBot: {respuesta}")

if __name__ == "__main__":
    main()