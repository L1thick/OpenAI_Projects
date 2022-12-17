import openai
from api_keys import OpenAIKey

# Add API to api_keys.py file.
openai.api_key = OpenAIKey

# Setup parameters.
prompt = input("Enter the prompt: ")
tokencount = 250
engine = "text-davinci-001"

# Question the God above.
aiOutput = openai.Completion.create(
    engine=engine, 
    prompt=prompt, 
    max_tokens=tokencount
)

# Dicipher the answer, please! 
valsOnly = list(aiOutput.values())
objOnly = valsOnly[4]                               # Displays aiOutput as a list.
lineOnly = objOnly[0]                               # Displays Objects JSON list.
lastOnly = lineOnly["text"]                         # Displays JUST the output for the prompt.
tokenTotals = valsOnly[5]                           # Displays all 3 tokens.
promptTokens = tokenTotals["completion_tokens"]     # Tokens used for this prompt
sessionTokens = tokenTotals                         # Tokens used for this prompt

# Display the Output.
print(lastOnly)
print("\n")
print("Tokens used this prompt: ")
print(promptTokens) 
