# main.py

from user_interface import display_artwork_options, interact_with_chatbot
from artworks_data import artworks

def main():
    while True:
        artwork_choice = display_artwork_options()
        if artwork_choice in artworks:
            interact_with_chatbot(artwork_choice)
        else:
            print("Sorry, we don't have that artwork in our museum.")
        
        another_artwork = input("\nWould you like to explore another artwork? (yes/no): ")
        if another_artwork.lower() != 'yes':
            print("\nThank you for visiting the Virtual Interactive Museum!")
            break

if __name__ == "__main__":
    main()
