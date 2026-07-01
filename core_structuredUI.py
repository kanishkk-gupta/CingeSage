import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="CineSage Analytics",
    page_icon="🎬",
    layout="centered"
)

# ---------------- Load Model ---------------- #

load_dotenv()

model = ChatMistralAI(model="mistral-small-2506")

# ---------------- Schema ---------------- #

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str

parser = PydanticOutputParser(pydantic_object=Movie)

# ---------------- Prompt ---------------- #

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
Extract movie information from the paragraph.

{format_instructions}
"""
        ),
        (
            "human",
            "{paragraph}"
        )
    ]
)

# ---------------- UI ---------------- #

st.title("🎬 CineSage Analytics")

st.markdown(
    "### Structured Output using LangChain + Pydantic Output Parser"
)

paragraph = st.text_area(
    "Movie Paragraph",
    height=220,
    placeholder="Paste a movie description here..."
)

if st.button("Extract Information"):

    if paragraph.strip() == "":
        st.warning("Please enter a paragraph.")
        st.stop()

    with st.spinner("Extracting..."):

        # EXACT SAME LOGIC

        final_prompt = prompt.invoke(
            {
                "paragraph": paragraph,
                "format_instructions": parser.get_format_instructions()
            }
        )

        response = model.invoke(final_prompt)

        structured_data = parser.parse(response.content)

    st.success("Extraction Complete ✅")

    st.markdown("---")

    st.subheader("📄 Raw LLM Output")

    st.code(
        response.content,
        language="json"
    )

    st.markdown("---")

    st.subheader("🐍 Parsed Pydantic Object")

    st.write(structured_data)