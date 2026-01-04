from dotenv import load_dotenv
import huggingface_hub, os

load_dotenv()  # THIS IS REQUIRED

print("hf hub:", huggingface_hub.__version__)
print("token loaded:", bool(os.getenv("HUGGINGFACEHUB_API_TOKEN")))

