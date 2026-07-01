# CineSage Analytics

### Right now your app prints nice text. And you will be doing it using Prompt templates.

---

CineSage Analytics is a media intelligence company that helps streaming platforms and production houses organize and analyze large volumes of movie data.

---

## Every day, the company receives:

- Movie descriptions
- Press releases
- Blog articles
- Review summaries
- Metadata from multiple sources

---

## But the problem is:

- The information is messy.
- It's unstructured.
- And it comes in long paragraphs.

---

Streaming platforms require structured movie metadata, yet most incoming data arrives as messy paragraphs. Extracting it manually is time-consuming, expensive, error-prone, and difficult to scale.

---

## CineSage wants to build an AI-powered tool that:

1. Takes a raw paragraph about a movie
2. Extracts important structured information
3. Generates a clean summary
4. Returns it in JSON format
5. Stores it in their database

---

# Today's Task

## Movie 1

### Paragraph

> Interstellar is a visually stunning science fiction epic directed by Christopher Nolan. Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain, and Michael Caine. The story revolves around a group of astronauts who travel through a wormhole near Saturn in search of a new home for humanity as Earth faces environmental collapse. The movie was widely appreciated for its emotional depth, scientific accuracy, and Hans Zimmer's powerful soundtrack. It holds a rating of 8.6 on IMDb and is often considered one of the greatest sci-fi films of the 21st century.

---

## Movie 2

### Paragraph

> The Dark Knight, released in 2008, is a superhero crime thriller directed by Christopher Nolan and produced by Warner Bros. The film features Christian Bale as Batman alongside Heath Ledger, Aaron Eckhart, and Gary Oldman. The plot focuses on Batman's battle against the chaotic criminal mastermind known as the Joker, whose actions plunge Gotham City into anarchy. Heath Ledger's performance earned widespread acclaim and a posthumous Academy Award. The film currently holds an IMDb rating of 9.0 and is praised for its intense storytelling and grounded realism.

---

## Movie 3

### Paragraph

> 3 Idiots is a 2009 Indian coming-of-age comedy-drama directed by Rajkumar Hirani. The film stars Aamir Khan, R. Madhavan, Sharman Joshi, Kareena Kapoor, and Boman Irani. Set in an engineering college, the story explores themes of friendship, academic pressure, and following one's passion rather than societal expectations. The movie became one of the highest-grossing Indian films of its time and received immense praise for its humor and emotional depth. It has a rating of 8.4 on IMDb and remains a cultural favorite across generations.

---

# But companies don't want text.

They want data they can store, search, filter, recommend, analyze, send to APIs.

That is called **Structured Output**.

So we will do this by using **Prompt Templates** and **Structured Output**.

---

# Solution

This project demonstrates two different approaches for extracting information from movie descriptions using **LangChain** and **Mistral AI**.

## 1. Prompt Templates

A simple Prompt Engineering approach where the LLM extracts useful movie information and generates a clean, human-readable response.

## 2. Structured Output

Uses LangChain's **Pydantic Output Parser** to force the LLM to return structured JSON that is automatically converted into a Python object.

---

# Project Structure

```
CineSage/
│
├── core_prompt.py
├── core_promptUI.py
├── core_structured.py
├── core_structuredUI.py
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

# Files Overview

## `core_prompt.py`

Demonstrates **Prompt Templates** using LangChain.

### Features

- Uses `ChatPromptTemplate`
- Accepts a movie paragraph as input
- Extracts useful movie information
- Generates a concise summary
- Returns a natural language response

---

## `core_promptUI.py`

A Streamlit interface for `core_prompt.py`.

### Features

- User-friendly web interface
- Paste a movie paragraph
- Displays extracted information
- Uses the same prompt template logic as `core_prompt.py`

---

## `core_structured.py`

Demonstrates **Structured Output** using LangChain.

### Features

- Defines a Pydantic `Movie` schema
- Uses `PydanticOutputParser`
- Forces the LLM to generate valid JSON
- Parses JSON directly into a Python object
- Prints:
  - Raw JSON response
  - Parsed Pydantic object

---

## `core_structuredUI.py`

A Streamlit interface for `core_structured.py`.

### Features

- Paste a movie paragraph
- View the raw JSON returned by the LLM
- View the parsed Pydantic object
- Demonstrates structured information extraction visually

---

# Technologies Used

- Python
- LangChain
- Mistral AI
- Streamlit
- Pydantic
- python-dotenv

---

# Concepts Covered

- Prompt Engineering
- ChatPromptTemplate
- Structured Prompting
- Pydantic Models
- Structured Output Parser
- Information Extraction
- JSON Generation
- Streamlit

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/CineSage.git
```

Move into the project

```bash
cd CineSage
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
MISTRAL_API_KEY=your_api_key
```

---

# Run Prompt Template

```bash
python core_prompt.py
```

Launch the Streamlit UI

```bash
streamlit run core_promptUI.py
```

---

# Run Structured Output

```bash
python core_structured.py
```

Launch the Streamlit UI

```bash
streamlit run core_structuredUI.py
```

---

# Learning Outcomes

After completing this project, you'll understand how to:

- Build prompt templates using LangChain
- Design reusable prompts
- Extract information from unstructured text
- Generate structured JSON using LLMs
- Parse JSON into Python objects using Pydantic
- Build simple AI-powered web applications using Streamlit

---

## Author

**Kanishk Gupta**

Built while learning **Generative AI**, **LangChain**, **Prompt Engineering**, and **Structured Output Parsing**.