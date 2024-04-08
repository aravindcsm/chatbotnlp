import nltk
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing fine, thank you!', 'I\'m good, thanks for asking.']),
    (r'what is your name?', ['You can call me ChatBot.', 'I\'m ChatBot, nice to meet you.']),
    (r'what are you doing',['going to college.','prepering for exams']),
    (r'Where are you from?',['im from hyd.','nizambad']),
    (r'What are your interests or hobbies?',['Coding and programming','Exploring new technologies'])
    # Add more patterns and responses as needed
]

# Create a Chat object
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Welcome to the chatbot! Type 'quit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
