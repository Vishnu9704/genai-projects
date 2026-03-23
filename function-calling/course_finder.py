import json
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv(override=True)
def search_courses(role,product,level):
    url="https://learn.microsoft.com/api/catalog/"
    params={"role":role,"product":product,"level":level}
    try:
        response=requests.get(url,params=params)
        modules_dict=response.json()
        return "\n".join(f"{m['title']} - {m['url']}" for m in modules_dict["modules"][0:5])
    except requests.exceptions.RequestException as e:
        return f"Unexpected error occured : {e}"
tools = [
   { 
       "type":"function",
       "function":{
      "name":"search_courses",
      "description":"Retrieves courses from the search index based on the parameters provided",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"The role of the learner (i.e. developer, data scientist, student, etc.)"
            },
            "product":{
               "type":"string",
               "description":"The product that the lesson is covering (i.e. Azure, Power BI, etc.)"
            },
            "level":{
               "type":"string",
               "description":"The level of experience the learner has prior to taking the course (i.e. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role","product","level"
         ]
      }
      }
   }
]
prompt1 = input("Enter your Input :")
messages = [{"role": "user", "content": prompt1}]
try:
    client = OpenAI(api_key=os.environ["GITHUB_TOKEN"],
                    base_url="https://models.inference.ai.azure.com")
    completion1 = client.chat.completions.create(model="gpt-4o-mini", messages=messages,tools=tools,tool_choice='auto')
    message_obj=completion1.choices[0].message
    if(message_obj.tool_calls):
        fn_name=message_obj.tool_calls[0].function.name
        args=json.loads(message_obj.tool_calls[0].function.arguments)
        available_functions={"search_courses":search_courses}
        fn_to_call=available_functions[fn_name]
        result=fn_to_call(**args)
        messages.append(message_obj)
        messages.append({"role":"tool","tool_call_id":message_obj.tool_calls[0].id,"name":fn_name,"content":result})
        completion2 = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        print(completion2.choices[0].message.content)
    else:
        print(message_obj.content)
except Exception as e:
    print("Exception", e)

