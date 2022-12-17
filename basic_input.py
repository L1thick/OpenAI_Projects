import openai
from api_keys import OpenAIKey

# Add API to api_keys.py file.
openai.api_key = OpenAIKey

# Setup parameters.
prompt = input("\nEnter the prompt: ")
tokencount = 250
engine = "text-davinci-001"

# Question the God above.
aiOutput = openai.Completion.create(
    engine=engine, 
    prompt=prompt, 
    max_tokens=tokencount
)

# Dicipher the answer, please! 
aiVals = list(aiOutput.values())
aiObj = aiVals[4]                                   # Displays aiOutput as a list.
lineOnly = aiObj[0]                                 # Displays Objects JSON list.
textOnly = lineOnly["text"]                         # Displays JUST the output for the prompt.
tokenTotals = aiVals[5]                             # Displays all 3 tokens use.
promptTokTol = tokenTotals["completion_tokens"]     # Tokens used for this prompt.
sessionTokens = tokenTotals["total_tokens"]         # Tokens used for this session.

# Display the Output.
print(textOnly)
print("\nTokens used this prompt: " + str(promptTokTol))
print("Tokens used this sessiont: " + str(sessionTokens) + "\n")