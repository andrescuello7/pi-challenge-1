import os
import openai

class ConfigOpenAI():
    def setApiCredentials():
        openai.api_type = os.getenv('OPENAI_TYPE')
        openai.api_version = os.getenv('OPENAI_VERSION')
        openai.api_key = os.getenv('OPENAI_KEY')
        openai.api_base = os.getenv('OPENAI_BASE')
    
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