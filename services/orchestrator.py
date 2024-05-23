from services.openai import config_openAI

# Configuración de las credenciales de OpenAI
config_openAI.set_api_credentials(self='')

def get_answer(history):
    _prompt = open("services/prompts/prompt_instructions.prompt", "r").read()

    # Configuración de las credenciales de OpenAI
    prompt = [{"role": "system", "content": _prompt}]
    history_item = [{"role": "user", "content": history["question"]}]

    # Obtener el historial de chat en formato de mensajes
    prompt.extend(history_item)

    # Solicitar una completación de chat a OpenAI
    completion = config_openAI.chat_completion(self='', prompt=prompt)

    # Extraer la respuesta generada por OpenAI
    response = completion["choices"][0]["message"]["content"]
    return {"data_points": "", "answer": response, "thoughts": ""}
