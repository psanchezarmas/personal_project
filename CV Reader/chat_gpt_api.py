import ipdb
import openai

openai.api_key = ""

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  
  messages=[
        {"role": "system", "content": "Can you classify the following text document into a json file?"}
        ]
  
)

print(response['choices'][0]['message'])
