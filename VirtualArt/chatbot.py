# chatbot.py

import random
from artworks_data import artworks

# Response functions for each type of information
def get_artist_info(artwork):
    return f"The artist of {artwork} is {artworks[artwork]['artist']}."

def get_creation_date(artwork):
    return f"{artwork} was created in {artworks[artwork]['year']}."

def get_artwork_description(artwork):
    return f"Description: {artworks[artwork]['description']}"

def get_historical_context(artwork):
    return f"The historical context of {artwork} is: {artworks[artwork]['historical_context']}."

def get_fun_facts(artwork):
    facts = artworks[artwork]['fun_facts']
    return random.choice(facts)  # Randomly selects a fun fact

# Main function to handle questions based on keywords
def handle_question(question, artwork):
    question = question.lower()
    if "artist" in question:
        return get_artist_info(artwork)
    elif "year" in question or "when" in question:
        return get_creation_date(artwork)
    elif "description" in question or "about" in question:
        return get_artwork_description(artwork)
    elif "historical context" in question:
        return get_historical_context(artwork)
    elif "fun fact" in question:
        return get_fun_facts(artwork)
    else:
        return "I'm sorry, I don't understand that question. Try asking about the artist, the year it was created, or a fun fact!"
