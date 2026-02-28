from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    
    name : str
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10, default=None, description='A decimal value representating CGPA')

new_student = {'name':'Charlie', 'age':'31', 'email':'abc@gmail.com', 'cgpa':7}

student = Student(**new_student)

#print(student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()

print(student_json)

# new we can throw the following error if data does not meet condition.


# pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
# name
#   Input should be a valid string [type=string_type, input_value=32, input_type=int]
#     For further information visit https://errors.pydantic.dev/2.12/v/string_type