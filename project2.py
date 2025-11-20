# Basic Rule-Based Chatbot

def respond_to_user(message):
    # Convert message to lowercase for easier matching
    message = message.lower()

    # Rule-based responses using if-elif
    if message == "hello" or message == "hi":
        return "Hello! How can I help you today?"
    elif message == "how are you":
        return "I'm doing great, thanks for asking!"
    elif message == "bye":
        return "Goodbye! Have a nice day!"
    elif message == "what is your name":
        return "I am ChatBot 1.0, your virtual assistant."
    else:
        return "Sorry, I didn't understand that. Can you try again?"

def chatbot():
    print("------ Welcome to Basic Chatbot ------")
    print("Type 'bye' anytime to exit.")
    print("--------------------------------------")

    while True:
        user_input = input("You: ")

        # Exit condition
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Get response and print
        reply = respond_to_user(user_input)
        print("Chatbot:", reply)


# Run the chatbot
chatbot()
