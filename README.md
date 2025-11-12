
# CookLogic | Smart Recipe Recommender 🥘

**CookLogic** is an AI-powered web application that helps you turn your available ingredients into delicious recipes. Simply enter the ingredients you have, and the app will generate a detailed recipe including the cooking time, step-by-step instructions, ingredients list, and optional tips. It’s designed to make cooking simple, fun, and logical.

## Features

* **AI-Generated Recipes:** Uses the power of **LangChain** and **ChatGroq LLM** to provide creative and practical recipes based on the ingredients you provide.
* **Interactive Web App:** Built with **Streamlit**, offering a smooth and responsive interface for a seamless user experience.
* **Search History:** Tracks your previous searches in the sidebar so you can quickly revisit past recipes.
* **Markdown Output:** Recipes are formatted in Markdown for easy readability and clear structure.
* **Clear History Option:** Reset your search history at any time for a fresh start.

## Tech Stack

* Python 3.x
* [Streamlit](https://streamlit.io/) for the frontend interface
* [LangChain](https://www.langchain.com/) with [ChatGroq](https://groq.com/) API for AI-powered recommendations

## How It Works

1. Users input ingredients separated by commas.
2. On submission, the app sends a prompt to the AI model specifying the ingredients and required recipe format.
3. The AI responds with a recipe including name, cooking time, ingredients, instructions, and optional tips.
4. Recipes are displayed in a clean Markdown format, while recent searches are stored in **session state** for quick access.

## Installation

1. Clone the repo and navigate to the project directory.
2. Install dependencies using `pip install -r requirements.txt`.
3. Add your **Groq API key** in the app code.
4. Run the app using `streamlit run app.py`.

## Future Improvements

* AI-generated recipe images
* Nutritional information for recipes
* Option to create shopping lists from generated recipes

CookLogic combines AI and interactive web development to help anyone cook smarter, using logic and creativity to turn simple ingredients into great meals.

---


