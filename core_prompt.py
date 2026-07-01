#We'll be using Chat prompts / templates to build this

from dotenv import load_dotenv
load_dotenv()


from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model= "mistral-small-2506")

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system",  
     """
You are an expert Information Extraction Assistant.

Your job is to carefully read the given text and identify the most important information.

Instructions:

• Read the entire text carefully before answering.
• Extract only information that is explicitly mentioned.
• Do not invent or assume facts.
• If some information is not available, simply write "Not Mentioned".
• Keep the response clear, organized, and concise.
• Preserve names, dates, numbers, and important entities exactly as written.
• Generate a brief summary at the end.

When possible, identify the following:

1. Title or Main Subject
2. Document Type (Movie, Book, Person, Product, Company, Event, Research Paper, Article, etc.)
3. Main Topic
4. Important People
5. Organizations
6. Locations
7. Dates and Years
8. Important Numbers or Statistics
9. Category or Genre (if applicable)
10. Key Attributes
11. Major Events or Highlights
12. Important Facts
13. Keywords
14. Overall Sentiment or Tone
15. A concise summary (2-4 sentences)

Present the information using clean headings and bullet points.
"""),
("human", 
 """
Analyze the following text and extract the most useful information.

Paragraph: 
{paragraph} 
""")
])


para = input("Give your paragraph: ")

final_prompt = prompt.invoke(
    {"paragraph" : para }
)

response = model.invoke(final_prompt)

print(response.content)
