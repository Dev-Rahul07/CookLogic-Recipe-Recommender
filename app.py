import streamlit as st
from langchain_groq import ChatGroq
import time

if "d" not in st.session_state:
    st.session_state.d = {}
st.set_page_config(page_title="CookLogic | Recipe Recommender", page_icon="🥘",initial_sidebar_state="expanded")



if st.sidebar.button("Clear History "):
    st.session_state.d = {}

def search_Hist():
    st.sidebar.markdown("### 🕒 Recent Searches")
    for item in reversed(list(st.session_state.d.keys())):
        if st.sidebar.button(item, key=item):
            st.markdown(st.session_state.d[item])




st.title("🥘 CookLogic || smart recipes, logical cooking")


groq_api_key = "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"

def generate_recommendations(input_text):
    try:
        llm = ChatGroq(
            temperature=0.7,
            groq_api_key=groq_api_key,
            model="llama-3.1-8b-instant"
        )

        prompt = f"""
        You are a friendly chef. Given these ingredients: {input_text},
        suggest a detailed recipe with:
        - Recipe Name
        - Estimated Cooking Time
        - Ingredients List
        - Step-by-step Instructions
        - Optional Tips
        Format the output nicely in Markdown.
        """

        response = llm.invoke(prompt)

        #Extract only the recipe text (ignore metadata)
        # Checks if the response object has an attribute called content.
        if hasattr(response, "content"):
            return response.content.strip()
        elif isinstance(response, dict) and "content" in response:
            return response["content"].strip()
        else:
            return str(response).split("content=")[-1].split("additional_kwargs")[0].strip()

    except Exception as e:
        st.error(f" An error occurred: {str(e)}")
        return None


# Form for user input
with st.form("my_form"):
    user_input = st.text_area("🍅 Enter your preferred ingredients (separated by commas):")
    submitted = st.form_submit_button("Get Recipe Recommendations")

# Run the model when user submits

if submitted:
    if groq_api_key.startswith("gsk_"):
        if user_input.strip():
            with st.spinner("🍳 Cooking up your recipe..."):
                recipe = generate_recommendations(user_input)
                st.session_state.d[user_input] = recipe
                
            if recipe:
                
    
                st.success("Recipe Ready!")
                st.markdown(recipe)  
        else:
            st.warning("Please enter some ingredients before submitting.")
            

            
search_Hist()

