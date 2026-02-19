from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage 
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

chat_history = [
    SystemMessage(content='You are a helpful assistent.'),
    
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)

'''
[
    'Hi', 
    'Hi there! How can I help you today?', 
    'which is greater 2 or 0', 
    '2 is greater than 0.', 
    'now multiply the greater number with 10', 
    "You're right!\n\n1.  **2** is greater than 0.\n2.  Multiplying the greater number (2) by 10 gives you **20**.", 'exit'
]

There is slight problem in this chart bot as we cannot see which responce is from AI AND
which is from user.
this can be solved by using langChain Messages.
    
'''