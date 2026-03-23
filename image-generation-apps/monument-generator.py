from openai import OpenAI
from dotenv import load_dotenv
import os
from openai import BadRequestError
from base64 import b64decode
from datetime import datetime

def save_image(decode):
    now=datetime.now()
    script_dir = os.path.dirname(__file__)
    image_dir = os.path.join(script_dir, "generated-images")
    image_path = os.path.join(image_dir, f"generated_image_{now.strftime("%Y%m%d_%H%M%S")}.png")
    os.makedirs(image_dir, exist_ok=True)
    with open(image_path, "wb") as binary_file:
        binary_file.write(decode)
    return f"{image_path} saved"


def generate_image(prompt,deployment_name,client):
    result=client.images.generate(prompt=prompt,model=deployment_name,quality='low',size='1024x1024').data[0].b64_json
    return result


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""
try:
    load_dotenv()
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    prompt=meta_prompt+input("Enter what you want : ")
    decode=b64decode(generate_image(prompt,"gpt-image-1-mini",client))
    print(save_image(decode))
except BadRequestError:
    print("API Loading Failed..Please try again with correct Inputs")
except Exception as err:
    print("Wrong",err)