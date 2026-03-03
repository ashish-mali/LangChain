# from dotenv import load_dotenv
# import huggingface_hub, os

# load_dotenv()  # THIS IS REQUIRED

# print("hf hub:", huggingface_hub.__version__)
# print("token loaded:", bool(os.getenv("HUGGINGFACEHUB_API_TOKEN")))

# Group the Employees by Department
emp = {
    "Rahul" : "HR",
    "Amit": "IT",
    "Neha": "IT",
    "Sita": "HR"
}

dict_ = {}

for e, d in emp.items():
    dict_.setdefault(d, []).append(e)

print(dict_)

