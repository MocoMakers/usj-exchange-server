import os
import openai
openai.api_key = "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"

def description_prompt(characteristics):
    ini_prompt = "Filter the following list of words to only items that are nouns: " + characteristics

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "user", "content": ini_prompt}, 
            {"role": "user", "content": "Create a facebook marketplace description of the object above that is no more than 50 words long."}
        ]
    )
    
    return response