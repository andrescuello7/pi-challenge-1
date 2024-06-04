from services.openai import config_openAI

# Settings credentials of OpenAI
config_openAI.set_api_credentials(self='')

def get_answer(history):
    _prompt = open("services/prompts/prompt_instructions.prompt", "r").read()
    prompt = [{"role": "system", "content": _prompt}]
    history_item = [{"role": "user", "content": history["question"]}]

    # Get historial
    prompt.extend(history_item)
    completion = config_openAI.chat_completion(self='', prompt=prompt)
    response = completion["choices"][0]["message"]["content"]
    return {"data_points": "", "answer": response, "thoughts": ""}
