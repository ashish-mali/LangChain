# from dotenv import load_dotenv
# import huggingface_hub, os

# load_dotenv()  # THIS IS REQUIRED

# print("hf hub:", huggingface_hub.__version__)
# print("token loaded:", bool(os.getenv("HUGGINGFACEHUB_API_TOKEN")))

# Group the Employees by Department
# emp = {
#     "Rahul" : "HR",
#     "Amit": "IT",
#     "Neha": "IT",
#     "Sita": "HR"
# }

# dict_ = {}

# for e, d in emp.items():
#     dict_.setdefault(d, []).append(e)

# print(dict_)

# Deployment testing 
'''
During development, you might want to test your application without making actual API calls.
LangChain providers FakeListLLM for this purpose
'''

from langchain_community.llms import FakeListLLM

# create a fake llm list that always returns the same response
fake_llm = FakeListLLM(responses=["Don't distrub me!!"])

result = fake_llm.invoke("Hey can you help to solve this bug?")

print(result)




