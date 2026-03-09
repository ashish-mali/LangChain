from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a 5 ponter summary from the following text \n {text}",
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model='models/gemini-2.5-flash')

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Optimize the SQL queries'})

print(result)

chain.get_graph().print_ascii()

'''
Here is a 5-pointer summary of the provided text:

1.  **Critical Importance:** SQL query optimization is essential for enhancing application performance, scalability, and cost-efficiency, directly impacting user experience and system throughput.
2.  **Multi-faceted Techniques:** Key optimization areas include strategic indexing (the most effective tool), efficient query rewriting (e.g., avoiding `SELECT *`, SARGable predicates, proper JOINs), robust database design, and optimal server configuration.
3.  **Tool-Driven Identification:** Effective optimization relies heavily on specialized tools like execution plan analyzers (`EXPLAIN`), database profilers, and performance monitoring tools to identify and understand query bottlenecks.
4.  **Systematic & Iterative Process:** It's an ongoing cycle of identifying, analyzing, optimizing, testing, and monitoring, rather than a one-time fix, requiring a deep understanding of database engine behavior.
5.  **Proactive & Ongoing Commitment:** Best practices involve proactive design, writing clean SQL, regular profiling, testing with realistic data, and avoiding pitfalls like premature optimization or over-indexing, emphasizing continuous improvement and developer education.
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
    +-----------------+
    | StrOutputParser |
    +-----------------+
             *
             *
             *
+-----------------------+
| StrOutputParserOutput |
+-----------------------+
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
    +-----------------+
    | StrOutputParser |
    +-----------------+
             *
             *
             *
+-----------------------+
| StrOutputParserOutput |
+-----------------------+

'''
