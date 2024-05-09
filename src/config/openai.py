import openai

class ConfigOpenAI():
    def setApiCredentials():
        openai.api_type = 'azure'
        openai.api_version = '2023-09-15-preview'
        openai.api_key = '82c826139c184423bcab26f62f4e621d'
        openai.api_base = 'https://gpt-pixie-db.openai.azure.com/'
    
    def ChatCompletion(prompt):
        return openai.ChatCompletion.create(
                    stop=["<|im_end|>", "<|im_start|>"],
                    top_p=0.2,
                    engine='gpt-pixie',
                    messages=prompt,
                    max_tokens=500,
                    temperature=float('0.0'))
    
    def Completion(gpt_deployment, prompt, n, stop):
        return openai.Completion.create(
                    engine='gpt-pixie', 
                    prompt=prompt, 
                    temperature=float('0.0'), 
                    max_tokens=500, 
                    n=n, 
                    stop=stop)