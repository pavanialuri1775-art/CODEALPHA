# CodeAlpha Python Tasks

This repository contains the Python tasks I completed during my CodeAlpha internship/training.

---

# 1. Rule-Based Chatbot

A simple chatbot built using Python that responds to user messages using predefined conditions.

## Features
- Responds to greetings
- Answers simple questions
- Ends conversation when user types "bye"
- Continuous interaction using a loop

## Code

```python
def greet(user_input):
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye"
    else:
        return "I don't understand."

while True:
    user = input("you: ")
    print(greet(user))

    if user == "bye":
        break
## Concepts Used
#- Functions
#- Conditional Statements
#- Loops
#- User Input Handling
#- String Comparison
## Author
#Pavani
