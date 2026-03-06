from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import structuredoutputparser, ResponseSchema


load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",  # safer choice
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='Fact 1 abount the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 abount the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 abount the topic'),
]

parser = structuredoutputparser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 facts abount {topic} \n {format_instruction}',
    input_variables = ['topic'],
    partial_variables={'format_instruction':parser.get_format_instruction()}
)

prompt = template.invoke({'topic':'black hole'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)

# This biggest dis-advantage of this aproch is we can't do data validation.

# This is depricated and not available in new version of langchain.
# we have to use the PydanticOutputParser.
