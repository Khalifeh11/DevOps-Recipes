import streamlit as st
import requests

# Your Spoonacular API Key
API_KEY = '5d86ae2ae1a7445197b50399b0b48788'  # Replace this with your actual key
API_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def fetch_recipes(ingredients):
    # Prepare query parameters
    params = {
        'ingredients': ingredients,
        'number': 5,  # Limit to 5 results for simplicity
        'apiKey': API_KEY
    }
    response = requests.get(API_URL, params=params)
    # Ensure the response is in JSON format and handle errors
    try:
        recipes = response.json()  # Parse JSON
        return recipes  # Should return a list of recipes
    except ValueError:
        st.error("Failed to parse the response from the API.")
        return None

st.title('Recipe Finder')

# User input
ingredients = st.text_input('Enter ingredients (comma-separated):')

if st.button('Search'):
    if ingredients:
        recipes = fetch_recipes(ingredients)


        if recipes:
            if isinstance(recipes, list):  # Ensure recipes is a list
                for recipe in recipes:
                    st.write(f"**{recipe.get('title', 'No Title')}**")
                    st.image(recipe.get('image', ''))
            else:
                st.error("Unexpected API response structure.")
        else:
            st.error('No recipes found or error occurred.')
    else:
        st.error('Please enter ingredients.')
