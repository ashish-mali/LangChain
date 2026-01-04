import os

# IMPORTANT: use raw string or double backslashes
os.environ["HF_HOME"] = r"D:\huggingface_cache"
os.environ["HUGGINGFACE_HUB_CACHE"] = r"D:\huggingface_cache\hub"
os.environ["TRANSFORMERS_CACHE"] = r"D:\huggingface_cache\transformers"

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={
        "temperature": 0.5,
        "max_new_tokens": 100
    }
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")
print(result.content)
