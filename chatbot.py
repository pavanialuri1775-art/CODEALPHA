#
def greet(user_input):
    if user_input=="hello":
        return "Hi!"
    elif user_input=="how are you":
        return "I'm fine, thanks!"
    elif user_input=="bye":
        return "Goodbye"
    else:
        return "I don't understand"
while True:
    user=input("You: ")

    print(greet(user))

    if user=="bye":
        break