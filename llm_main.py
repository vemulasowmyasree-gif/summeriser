from openai import OpenAI
import os
from prompts import summerize_prompt  
from constants import OPENAI_API_KEY

def summarizer(user_input):
    final_prompt= summerize_prompt .format(paragraph= user_input)
    client = OpenAI(api_key= OPENAI_API_KEY)
    response = client.responses.create(
        model="gpt-4o-mini",
        input= final_prompt,
        #temperature= 2
    )
    print(response.output_text)
    return response.output_text