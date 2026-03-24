from openai import OpenAI
from dotenv import load_dotenv
import logging
import os

load_dotenv(override=True)

client = OpenAI(api_key=os.environ["GITHUB_TOKEN"],
                base_url="https://models.inference.ai.azure.com")
deployment_name="gpt-4o-mini"
prompt1 = "You are an expert Python tutor. Answer any Python-related questions the user asks. You can explain concepts, show code examples, give exercises with solutions, and help debug code. If the user asks about anything not related to Python, politely tell them you can only help with Python-related questions."
messages = [{"role": "system", "content": prompt1}]
print("Welcome to Study Buddy! I'm your AI-powered Python tutor. Feel free to ask any questions you have about Python. If you want to exit at any time, just type 'exit' \n")

while(True): 
    question=input("Question ? ")
    if question.lower()=="exit":
        print("Good Bye ..✋🏻✋🏻✋🏻")
        break
    elif(len(question.split(" "))>500):
        print("The maximum input Limit is reached please try again entering upto maximum of 500 words")
        continue
    try:
        print("Loading📖📖📖....   Please Wait")
        messages.append({"role":"user","content":question})
        completion1 = client.chat.completions.create(model=deployment_name, messages=messages,temperature=0.1,max_completion_tokens=300,stream=True)
        result = ""
        for chunk in completion1:
            if chunk.choices:
                delta = chunk.choices[0].delta.content
                if delta:
                    print(delta, end="")
                    result += delta
        messages.append({"role":"assistant","content":result})
        print()
    except Exception as e:
        print(f"We are having trouble Connecting....We will be right back after fixing it. So please try again after some time.")
        logging.error(e)
        messages.pop()
