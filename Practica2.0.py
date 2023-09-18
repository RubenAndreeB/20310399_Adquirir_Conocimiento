# -*- coding: utf-8 -*-
"""
Ruben Andree Barba Magdaleno 20310399 7F

Chat bot con adquisión de conocimiento.
"""

import json
from difflib import get_close_matches

def cargar_base_conocimiento(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def guardar_base_conocimiento(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
def buscar_mejor_coincidencia(pregunta_usuario: str, preguntas: list[str]) -> str or None:
    matches: list = get_close_matches(pregunta_usuario, preguntas, n=1, cutoff=0.6)
    return matches[0] if matches else None
    
def genererar_respuesta (pregunta: str, base_conocimiento: dict) -> str or None:
    for q in base_conocimiento["preguntas"]:
        if q["pregunta"] == pregunta:
            return q["respuesta"]
        
def chat_bot():
    base_conocimiento: dict = cargar_base_conocimiento('base_conocimiento.json')
    
    while True:
        entrada_usuario: str = input('Tu: ')
        
        if entrada_usuario.lower() == 'salir':
            break
        
        mejor_coincidencia: str or None = buscar_mejor_coincidencia(entrada_usuario, [q["pregunta"] for q in base_conocimiento["preguntas"]])
        
        if mejor_coincidencia:
            respuesta: str = genererar_respuesta(mejor_coincidencia, base_conocimiento)
            print(f'Bot: {respuesta}')
        else:
            print('Bot: No conozco la respuesta, puedes enseñarme?')
            nueva_respuesta: str = input('Escribe la respuesta o escribe "skip" para omitir: ')
            
            if nueva_respuesta.lower() != 'skip':
                base_conocimiento["preguntas"].append({"pregunta": entrada_usuario, "respuesta": nueva_respuesta})
                guardar_base_conocimiento('base_conocimiento.json', base_conocimiento)
                print('Bot: Gracias! Aprendí una nueva respuesta')
                
if __name__ == '__main__':
    print('Bienvenido a chatGPT 8, escribe "salir" para abandonar el chat.')
    chat_bot()