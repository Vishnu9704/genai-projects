import json
from os import environ
from dotenv import load_dotenv
from openai import OpenAI
import numpy as np

load_dotenv(override=True)
def cosine_similarity(a,b):
    return np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))

with open("embedding_index_3m.json") as f:
    data=json.load(f)
    print(len(data))
client =OpenAI(api_key=environ["GITHUB_TOKEN"],base_url="https://models.inference.ai.azure.com")
deplyment_name="text-embedding-3-small"
prompt=input("Enter Question ? ")
response=client.embeddings.create(input=prompt,model=deplyment_name)
question_embedding=response.data[0].embedding
for i in data:
    i["similarity"]=cosine_similarity(question_embedding,i["ada_v2"])
data.sort(key=lambda x:x["similarity"],reverse=True)
for item in data[0:3]:
    print(f"{item["title"]}Link https://www.youtube.com/watch?v={item["videoId"]}&t={item["seconds"]}")

