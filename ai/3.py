responses = {
    "hello": "Hi!",
    "how are you": "I'm fine."
}

user = input("You: ")
print(responses.get(user.lower(), "I don't understand"))