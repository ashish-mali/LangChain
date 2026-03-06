from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

# schema
class Review(TypedDict):
    summary : str
    sentiment : str

structured_model = model.with_structured_output(Review)



result = structured_model.invoke(
    '''
    The ardware is great, but the software feels bloated. there are too mnay pre-installed
    apps that I can't remove. Also, the UI lloks outdated compared to toher brands.
    Hoping for a softwar update to fix this.
    '''
)

print(result)

# print(result['sentiment'])

# print(result['summary'])