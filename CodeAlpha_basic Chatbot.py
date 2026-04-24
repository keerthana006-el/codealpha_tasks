def chatbot():
    """Simple rule-based chatbot function"""
    print("🤖 Chatbot: Hello! Say 'hello', 'how are you', 'bye', or 'quit' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        if user_input in ['hello', 'hi', 'hey']:
            print("🤖 Chatbot: Hi! 👋")
        elif user_input in ['how are you', 'how r u', 'how do you do']:
            print("🤖 Chatbot: I'm fine, thanks! How about you? 😊")
        elif user_input in ['bye', 'goodbye', 'see you', 'exit']:
            print("🤖 Chatbot: Goodbye! 👋 Have a great day!")
            break
        elif user_input == 'quit':
            print("🤖 Chatbot: See you later! 👋")
            break
        else:
            print("🤖 Chatbot: Sorry, I don't understand. Try 'hello', 'how are you', or 'bye'.")
        
        print() 

if __name__ == "__main__":
    chatbot()