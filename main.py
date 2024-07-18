from openai import OpenAI 
import httpx
client = OpenAI()

no_recipes = input ("No of recipes (for example, 5: ")
ingredients = input ("List of ingredients (for example, chicken, potatoes, and carrot: ")
filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

prompt1 = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"

#prompt="Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
  
messages=[
   # {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
     {"role": "system", "content": prompt1}
   # {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
  )

prompt1_result = completion.choices[0].message.content

prompt2 = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

prompt2_result = f"{prompt1_result} {prompt2}"
messages = [{"role": "user", "content": prompt2_result}]
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(prompt1_result)
print(completion.choices[0].message.content)