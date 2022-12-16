import openai
from api_keys import OpenAI

openai.api_key = OpenAI

prompt = " "

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=250)

print(response)