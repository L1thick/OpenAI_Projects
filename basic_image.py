import openai
from api_keys import OpenAIKey

openai.api_key = OpenAIKey

prompt = " "

response = openai.Image.create(
    prompt=prompt,
    n=1,
    size="256x256"
)

urlOnly = response["data"]

print(urlOnly)
