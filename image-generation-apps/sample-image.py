from openai import OpenAI
from dotenv import load_dotenv
import os
from openai import BadRequestError
from base64 import b64decode

def save_image(decode):
    script_dir = os.path.dirname(__file__)
    image_dir = os.path.join(script_dir, "generated-images")
    image_path = os.path.join(image_dir, "file1.png")
    os.makedirs(image_dir, exist_ok=True)
    with open(image_path, "wb") as binary_file:
        binary_file.write(decode)
def generate_image(prompt,deployment_name,client):
    result=client.images.generate(prompt=prompt,model=deployment_name,quality='low',size='1024x1024').data[0].b64_json
    return result
try:
    load_dotenv()
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"],
                    base_url="https://api.openai.com/v1/")
    deployment_name="gpt-image-1-mini"
    decode=b64decode(generate_image(input("Enter what you want : "),deployment_name,client))
    save_image(decode)
except BadRequestError:
    print("API Loading Failed..Please try again with correct Inputs")
except Exception as err:
    print("Wrong",err)