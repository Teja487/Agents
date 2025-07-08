from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm = ChatOpenAI(model="gpt-4o")

class Country(BaseModel):
    """Information about the Country"""
    name: str = Field(description="name of the country")
    language: str = Field(description="language of the country")
    capital: str = Field(description="capital of the country")
    bird: str = Field(description="National bird of the country")

structured_llm = llm.with_structured_output(Country)
#print(structured_llm)

respomse = structured_llm.invoke("Tell me about India")
print(respomse)
