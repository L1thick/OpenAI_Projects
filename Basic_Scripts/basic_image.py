import openai
from api_keys import OpenAIKey

# Add API to api_keys.py file.
openai.api_key = OpenAIKey

# Setup parameters.
prompt = input("\nEnter the prompt: ")
size = "256x256"
amount = 1

# Generate the Image request.
creation = openai.Image.create(
    prompt=prompt,
    n=amount,
    size=size
)

# Extract URL from OpenAI reply. 
imgData = creation["data"]          # Displays output information.
urlOnly = imgData[0]                # Displays output JSON list.
linkURL = urlOnly["url"]            # Displays the raw URL from the export.

# Output the raw URL.
print("\n" + str(linkURL))

## TO DO
#
# Download URL to running users desktop
#
# Creat menu for parameter input & size selection