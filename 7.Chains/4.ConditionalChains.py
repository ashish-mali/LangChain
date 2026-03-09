from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda, RunnableBranch
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

class Feedback(BaseModel):
    
    sentiment : Literal['positive', 'negative'] = Field(description='Give the sentiment of thefeedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)


classifier_chain = prompt1 | model | parser2


prompt2 = PromptTemplate(
    template='Write an apporiate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x : 'Could not find sentiment')
)

chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()

'''
Here are several options for an appropriate response to positive feedback, ranging in tone and length. Choose the one that best fits your brand voice and the specific context.

**Key elements to include:**

*   **Thank the person:** Always start with gratitude.
*   **Acknowledge the positive experience:** Show you heard them.
*   **Reinforce your value:** Briefly mention what you strive for.
*   **Encourage continued engagement (optional):** Invite them back or to share.

---

**1. Short & Sweet:**
> "Thank you so much for your kind words! We're thrilled to hear you had a positive experience."

**2. Standard & Professional:**
> "We truly appreciate you taking the time to share your positive feedback. We're delighted to know you had such a great experience with [our product/service/team]."

**3. Enthusiastic & Warm:**
> "That's fantastic to hear! We're absolutely thrilled you had such a positive experience. Your feedback made our day!"

**4. With a Call to Action (Subtle):**
> "Thank you for your amazing feedback! We're so glad you enjoyed [mention a specific aspect if you know it, otherwise 'your experience']. We look forward to serving you again soon!"

**5. Emphasizing Team Effort:**
> "We truly appreciate your kind words! It means a lot to our team to know that our efforts to [provide excellent service/create a great product/etc.] are appreciated."

**6. For Social Media/Quick Reply:**
> "Wonderful to hear! Thank you for the positive feedback! 😊"

---

**When choosing, consider:**

*   **The platform:** A quick tweet might use option 6, while an email might use option 2 or 3.
*   **Your brand voice:** Are you formal, casual, friendly, luxurious?
*   **The specific feedback (if you have more details):** If they praised something specific (e.g., "the quick delivery"), you can incorporate that: "We're so glad you appreciated the quick delivery!"

Always aim for a genuine and appreciative tone!
      +-------------+      
      | PromptInput |
      +-------------+
             *
             *
             *
    +----------------+
    | PromptTemplate |
    +----------------+
             *
             *
             *
+------------------------+
| ChatGoogleGenerativeAI |
+------------------------+
             *
             *
             *
 +----------------------+
 | PydanticOutputParser |
 +----------------------+
             *
             *
             *
        +--------+
        | Branch |
        +--------+
             *
             *
             *
     +--------------+
     | BranchOutput |
     +--------------+
'''
