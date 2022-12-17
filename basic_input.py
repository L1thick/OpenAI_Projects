import openai
from api_keys import OpenAIKey

openai.api_key = OpenAIKey

prompt = " "

response = openai.Completion.create(engine="text-davinci-001", prompt=prompt, max_tokens=250)

print(response)