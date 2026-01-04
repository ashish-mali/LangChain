from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Sachin Tendulkar is known as the God of Cricket for his unmatched consistency and longevity.",
    "MS Dhoni is admired for his calm leadership and finishing skills under pressure.",
    "Virat Kohli is celebrated for his aggressive mindset and exceptional batting records.",
    "Rohit Sharma is famous for his elegant batting and ability to score big hundreds.",
    "Kapil Dev is remembered for leading India to its first World Cup victory in 1983."
]


query = 'tell me about rohit sharma'

doc_embeddings = embedding.embed_documents(documents)

query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0] # should be 2d vector

index, score =  sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(f'User : {query}')
print(documents[index])
print(f'Similarity Score: {score}')
