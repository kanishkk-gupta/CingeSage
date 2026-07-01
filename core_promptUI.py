import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

# -------------------- CONFIG --------------------

st.set_page_config(
    page_title="Information Extractor",
    page_icon="📄",
    layout="wide"
)

load_dotenv()

# -------------------- API KEY --------------------

st.sidebar.title("🔑 Configuration")

api_key = st.sidebar.text_input(
    "Enter your Mistral API Key",
    type="password",
    placeholder="Paste your API Key here..."
)

st.sidebar.markdown(
    "[Get your Mistral API Key](https://console.mistral.ai/api-keys)"
)

api_key = api_key or os.getenv("MISTRAL_API_KEY")

if not api_key:
    st.warning("👈 Please enter your Mistral API Key from the sidebar.")
    st.stop()

model = ChatMistralAI(
    model="mistral-small-2506",
    api_key=api_key
)

# -------------------- PROMPT --------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
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
2. Document Type
3. Main Topic
4. Important People
5. Organizations
6. Locations
7. Dates and Years
8. Important Numbers or Statistics
9. Category or Genre
10. Key Attributes
11. Major Events or Highlights
12. Important Facts
13. Keywords
14. Overall Sentiment or Tone
15. A concise summary (2-4 sentences)

Present the information using clean headings and bullet points.
"""
    ),
    (
        "human",
        """
Analyze the following text and extract the most useful information.

Paragraph:

{paragraph}
"""
    )
])

# -------------------- CSS --------------------

st.markdown("""
<style>

.main{
    padding-top:2rem;
}

.title{
    text-align:center;
    font-size:3rem;
    font-weight:700;
    margin-bottom:0;
}

.subtitle{
    text-align:center;
    color:#8b8b8b;
    font-size:1.1rem;
    margin-bottom:2rem;
}

.stTextArea textarea{
    border-radius:18px;
    font-size:16px;
    padding:18px;
}

.stButton>button{
    width:100%;
    border-radius:12px;
    height:3.2rem;
    font-size:18px;
    font-weight:600;
}

.output-card{
    padding:25px;
    border-radius:18px;
    background:#111827;
    border:1px solid #2b2b2b;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------

st.markdown(
    '<p class="title">📄 Information Extractor</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Extract structured insights, important entities, and a concise summary from any paragraph.</p>',
    unsafe_allow_html=True
)

# -------------------- INPUT --------------------

paragraph = st.text_area(
    "Enter your paragraph",
    height=280,
    placeholder="Paste any paragraph here..."
)

# -------------------- BUTTON --------------------

if st.button("✨ Extract Information"):

    if paragraph.strip() == "":
        st.warning("Please enter a paragraph.")
        st.stop()

    with st.spinner("Analyzing..."):

        final_prompt = prompt.invoke(
            {
                "paragraph": paragraph
            }
        )

        response = model.invoke(final_prompt)

    st.markdown(
        '<div class="output-card">',
        unsafe_allow_html=True
    )

    st.markdown("## 📑 Extracted Information")

    st.markdown(response.content)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )
