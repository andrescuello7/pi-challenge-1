import os
from src.config.openai import ConfigOpenAI

# Configuración de las credenciales de OpenAI
ConfigOpenAI.setApiCredentials()

def get_answer(history):
    PROMPT_INSTRUCTIONS_FILE = f"src/orc/prompts/prompt_instructions.prompt"
    prompt_schema = open(PROMPT_INSTRUCTIONS_FILE, "r").read()

    # Configuración de las credenciales de OpenAI
    prompt = [{"role": "system", "content": prompt_schema}]
    history_item = [{"role": "user", "content": history["question"]}]
        
    # Obtener el historial de chat en formato de mensajes
    prompt.extend(history_item)
        
    # Solicitar una completación de chat a OpenAI
    completion = ConfigOpenAI.ChatCompletion(prompt=prompt)
        
    # Extraer la respuesta generada por OpenAI
    response = completion["choices"][0]["message"]["content"]
    return {"data_points": "", "answer": response, "thoughts": ""}
