#We'll be using Structured prompts 

from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()
model = ChatMistralAI(model= "mistral-small-2506")


class Movie(BaseModel): #inherit basemodel class for creating pydantic schema
    title: str 
    release_year: Optional[int]
    genre: List[str] #genre may be many for the same movie so we kept it inside movie
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary : str

parser = PydanticOutputParser(pydantic_object=Movie)





prompt = ChatPromptTemplate.from_messages(
    [("system", """ 
Extract movie information from the paragraph 
     {format_instructions}
"""),
("human", "{paragraph}")]
)



para = input("Give your paragraph: ")

final_prompt = prompt.invoke(
    {"paragraph" : para,
     "format_instructions" : parser.get_format_instructions() }
)

response = model.invoke(final_prompt)
structured_data = parser.parse(response.content)

print(response.content)
print(structured_data)

