from  langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash', temperature = 1)

result = model.invoke('Write the 5 line poem on python developer in hindi.')

print(result.content)