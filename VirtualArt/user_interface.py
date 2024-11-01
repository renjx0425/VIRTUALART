# user_interface.py

from artworks_data import artworks
from chatbot import handle_question

def display_artwork_options():
    print("Welcome to the Virtual Interactive Museum!")
    print("Here are the artworks you can explore:")
    for artwork in artworks.keys():
        print(f"- {artwork}")
    choice = input("Which artwork would you like to explore? Type the name exactly as shown above: ")
    return choice

def interact_with_chatbot(artwork):
    print(f"\nYou are now viewing: {artwork}")
    print("Ask me anything about it! Type 'exit' to leave this artwork.\n")
    while True:
        question = input("Your question: ")
        if question.lower() == 'exit':
            print(f"\nLeaving {artwork}...")
            break
        response = handle_question(question, artwork)
        print(response)
