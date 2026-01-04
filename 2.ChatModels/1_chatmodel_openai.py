from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4.1')

result = model.invoke("What is the cpatital of India?")

print(result.content)