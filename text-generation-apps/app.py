from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.environ["GITHUB_TOKEN"],
                base_url="https://models.inference.ai.azure.com")

deployment_name="gpt-4o-mini"

no_recipes = input("No of recipes (for example, 5): ")

ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

prompt1 = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"

messages = [{"role": "user", "content": prompt1}]

completion1 = client.chat.completions.create(model=deployment_name, messages=messages)

result=completion1.choices[0].message.content

prompt2="We want to produce a shopping list, considering what we already have at home {ingredients}"
message=[{"role": "user", "content": prompt1},
         {"role": "assistant", "content": result},
         {"role": "user", "content": prompt2}]
completion2=client.chat.completions.create(model=deployment_name,messages=message)

print(completion2)
