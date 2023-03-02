import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "Could you summarize the book 'Speculative Everything' by Anthony Dunne and Fiona Raby?"}
  ]
)

print(completion.choices[0].message)