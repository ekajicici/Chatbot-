from difflib import get_close_matches
import responses
from responses import generate_password, get_time, get_date
from rps_game import play_game


# Chatbot response dictionary
chatbot_responses = {
    "what is your name": "I'm Wonder-bot, but you can call me Shanice ;)",
    "how are you": "I'm great! Thanks for asking.",
    "hello": "Hey there!",
    "hi": "Wagwan!",
    "hey": "Howdy!",
    "goodbye": "See you later!",
    "nice to meet you": "The pleasure is all mine!",
    "how to learn coding": "Start by typing: 'How to learn coding' on Google.",
    "i'm hungry": "Go to the kitchen make something or order food",
    "Do you have feelings?": "I try to, but my code doesn't allow me to cry... yet",
    "Tell me a fun fact": "Did you know that honey never spoils? Just like my sense of humor!",
    "tell me a joke": "YO Mama!",
    "who are you": "I am a Chosen oh, I am a Chosen."
}


def get_response(input_string):
    """
      Returns an appropriate response based on user input.
      The argument 'input string' is the input provided by the user.
      It returns a response string based on the closest match in `chatbot_responses`
      or a default response if no match is found.
    """
    # Special cases for time, date, and password
    if "time" in input_string.lower():
        return get_time()
    if "date" in input_string.lower():
        return get_date()
    if "password" in input_string.lower() and "generate" in input_string.lower():
        return generate_password()
    if "game" in input_string.lower():
        return play_game()

    if input_string == "":  # This checks if the user input is empty
        return "Please, type something so we can chat."

    # This uses difflib's get_close_matches to find the closest match to user input
    closest_match = get_close_matches(input_string.lower(), chatbot_responses.keys(), n=1)
    if closest_match:
        key = closest_match[0]
        response = chatbot_responses[key]

        # This checks if the response is a callable function the calls the function and return the result
        if callable(response):
            return response()
        else:
            return response
    else:
        # Default responses if no close match is found
        return responses.default_response()


print("Hey! I'm your chatbot, powered by coffee and code.")
print("Faster than a search engine, cooler than your last browser tab!")
# This starts the chat loop to continuously interact with the user
while True:
    user_input = input("You: ")  # This gets the user input
    if user_input == "exit":
        print("Wonder-Bot: Goodbye!")  # It exits if the user types 'exit'
        break
    else:
        response = get_response(user_input)  # It gets the chatbot response based on user input and print it
        print(f"Wonder-Bot: {response}")  # This will respond to the user based of the input

