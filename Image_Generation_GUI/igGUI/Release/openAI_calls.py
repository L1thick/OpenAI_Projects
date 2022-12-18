import re
import string
import os.path
from api_keys import OpenAIKey
from os import path

def PrintMenu():
    print("====================================================")
    print("|          OpenAI API Connection CLI/GUI           |")
    print("|==================================================|")
    print("| 1: Menu item one.                                |")
    print("| 2: Menu item two.                                |")
    print("| 3: Menu item three.                              |")
    print("| 4: Exit the Program.                             |")
    print("|--------------------------------------------------|")
    print("| Enter your selection as a number: 1, 2, 3, or 4. |")
    print("====================================================")
    print("\nCurrent API key from file: " + OpenAIKey)                  # DEV NOTE

def twoFiveSix():
    print('test')