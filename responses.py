import random
import datetime


# Function to provide a default response when chatbot doesn't understand the user input
def default_response():

    random_list = [
        "I do not have any knowledge on the subject matter",
        "Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
    ]
    # This gets the length of the list to ensure proper range for random selection
    list_count = len(random_list)
    # This randomly selects an index from the list and return the corresponding message
    random_item = random.randrange(list_count)

    return random_list[random_item]


# Function to get the current time in 12-hour AM/PM format
def get_time():
    return datetime.datetime.now().strftime("%I:%M%p")


# Function to get the current date
def get_date():
    return datetime.datetime.now().strftime("%A, %dth %B %Y")


# Function to generate a strong password
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?"
    password = "".join(random.sample(chars, 12))  # it uses random.sample to ensure unique characters in the password;
    return password

