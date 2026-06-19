def chatbot():
    print("AI Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("AI: Hi! How are you?")
        elif user == "how are you":
            print("AI: I am fine. How can I help you?")
        elif user == "what is your name":
            print("AI: I am a Python AI Chatbot.")
        elif user == "bye":
            print("AI: Goodbye!")
            break
        else:
            print("AI: Sorry, I don't understand that.")

chatbot()