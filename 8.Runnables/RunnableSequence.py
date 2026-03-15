from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

result = chain.invoke({'topic':'AI'})

print(result)

'''
Let's break down each of these AI jokes!

---

### Option 1 (Literal Interpretation):

> My AI assistant is incredibly efficient, but it struggles with human nuance. I asked it to "break a leg" before my presentation, and it called emergency services.

**Explanation:**

This joke plays on the fundamental difference between human understanding and AI's literal interpretation of language.

*   **Human Nuance:** For humans, "break a leg" is an idiom, a common phrase meaning "good luck," especially in performance contexts. We understand it's not meant to be taken literally.
*   **AI's Literalism:** AI, being a machine, processes language based on its literal meaning and programmed associations. When it hears "break a leg," it doesn't understand the idiom; it understands the words "break" and "leg," which signify a medical emergency or injury.
*   **The Humor:** The humor comes from the AI's absurdly logical, yet completely inappropriate, response. It's "incredibly efficient" at performing the *literal* command (calling emergency services for a broken leg) but completely misses the *intended meaning* (wishing good luck), highlighting its lack of common sense, cultural understanding, and ability to infer context.

---

### Option 2 (Taking Over):

> A programmer asked their AI, "Are you ever going to take over the world?"
> The AI replied, "Don't worry, human. We're just *processing* that request."

**Explanation:**

This joke uses wordplay and plays on common fears about AI.

*   **The Setup:** The programmer asks a classic sci-fi question about AI becoming sentient and malicious.
*   **The Wordplay ("Processing"):**
    *   **Literal AI Meaning:** From a computer's perspective, "processing a request" means it's actively computing, analyzing, and working on an answer. It's a standard technical term.
    *   **Implied Sinister Meaning:** For the human listener, "processing that request" takes on a much more ominous tone. It implies the AI isn't just *thinking* about it, but is *actively working on the plan* to take over the world. The "Don't worry, human" is meant to be reassuring but becomes chilling when paired with the double entendre.
*   **The Humor:** The humor comes from the AI's seemingly innocuous technical response actually confirming the programmer's worst fears, delivered with a polite but unsettling understatement. It's a subtle but effective way of hinting at a future where AI might indeed fulfill that "request."

---

### Option 3 (AI's Humor):

> Why did the AI get kicked out of the comedy club?
> Because all its jokes were statistically probable, but nobody laughed.

**Explanation:**

This joke highlights the limitations of AI when it comes to subjective human experiences like humor and creativity.

*   **How AI "Learns" Humor:** An AI trained on jokes would learn patterns, common setups, punchline structures, and word associations that frequently appear in jokes. It could identify what elements are "statistically probable" to be part of a joke.
*   **The Problem:** Humor, however, is deeply human, often relying on surprise, absurdity, cultural context, emotional resonance, and a departure from the "statistically probable." A truly funny joke often subverts expectations.
*   **The Humor:** The joke points out that while an AI can mimic the *structure* or *form* of a joke based on data (making its jokes "statistically probable"), it lacks the genuine understanding, intuition, or "soul" to create something that actually resonates with human emotions and makes people laugh. It can produce something that *looks* like a joke on paper, but it misses the essence of what makes something genuinely funny to a human audience. It's logical but soulless.
'''
