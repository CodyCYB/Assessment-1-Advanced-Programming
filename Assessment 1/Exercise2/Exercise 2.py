import random
import os

def load_jokes(file_path="jokes.txt"):
    jokes = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, file_path)
    
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if "?" in line:
                    setup, punchline = line.split("?", 1)
                    jokes.append((setup + "?", punchline.strip()))

        if not jokes:
            print(f"No jokes found in the file: {full_path}")
    except FileNotFoundError:
        print(f"Error: The file was not found at: {full_path}")
        print("Put your jokes.txt next to the script or pass the full path to load_jokes().")
        return []
    return jokes

def say_joke(jokes):
    joke = random.choice(jokes)
    setup, punchline = joke
    print("\nAlexa: " + setup)
    while True:
        resp = input("You (type 'what' or 'why' to hear the punchline): ").strip().lower()
        if resp in ("what", "why"):
            print("Alexa: " + punchline + "\n")
            break
        else:
            print("Please type 'what' or 'why' to continue.")

def main():
    jokes = load_jokes("jokes.txt")
    if not jokes:
        return

    print("Welcome! say 'tell me a joke' to hear a joke or 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "tell me a joke":
            say_joke(jokes)
        elif user_input == "exit":
            print("Goodbye!")
            break
        else:
            print("Please try again with 'tell me a joke' or 'exit'.\n")

if __name__ == "__main__":
    main()
