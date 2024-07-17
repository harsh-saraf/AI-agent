from openai import OpenAI
client = OpenAI()

no_recipes


prompt="Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
  
messages=[
   # {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
     {"role": "system", "content": prompt}
   # {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

print(completion.choices[0].message.content)