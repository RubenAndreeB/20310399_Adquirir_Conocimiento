# Base de datos de respuestas predefinidas
respuestas_predefinidas = {
    "Hola": "¡Hola! ¿Cómo puedo ayudarte hoy?",
    "¿Cómo estás?": "Estoy aquí para responder tus preguntas. ¿En qué puedo ayudarte?",
    "De qué te gustaría hablar?": "Puedo hablar sobre una variedad de temas. ¿Tienes algo en mente?",
    "Estoy bien, ¿y tú?": "¡Me alegra escucharlo! ¿En qué puedo ayudarte?",
    "¿Qué es la inteligencia artificial?": "La inteligencia artificial es una rama de la informática que se enfoca en crear máquinas capaces de realizar tareas que requieren inteligencia humana.",
    "Gracias": "Es todo un placer para mí el ayudarte :)",
    "Salir": "¡Hasta luego! Gracias por chatear conmigo."
}

def chat_bot(pregunta):
    # Buscar una respuesta predefinida
    respuesta = respuestas_predefinidas.get(pregunta)

    if respuesta:
        return respuesta
    elif pregunta.lower() == "salir":
        return "Salir"  # Si el usuario ingresa "Salir", se devuelve esta respuesta especial
    else:
        # Si no se encuentra una respuesta predefinida, pedir al usuario que ingrese conocimiento nuevo.
        nuevo_conocimiento = input("Lo siento, no sé la respuesta. ¿Puedes proporcionarme información sobre eso? ")

        # Agregar el nuevo conocimiento a la base de datos
        respuestas_predefinidas[pregunta] = nuevo_conocimiento
        return "¡Gracias por compartir tu conocimiento!"

# Bucle principal del chat
while True:
    entrada = input("Tú: ")
    if entrada.lower() == "salir":
        print("Bot: ¡Hasta luego! Gracias por chatear conmigo.")
        break  # Salir del bucle si el usuario ingresa "Salir"
    salida = chat_bot(entrada)
    print("Bot:", salida)   