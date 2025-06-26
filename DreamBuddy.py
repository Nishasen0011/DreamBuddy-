print("🤖 Hello! I’m DreamBuddy. Ask me anything about studies or motivation.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("DreamBuddy: Hey there! Ready to learn something new today? 😊")

    elif "motivate" in user_input or "motivation" in user_input:
        print("DreamBuddy: Believe in yourself! You’re doing great, and every step matters. 🚀")

    elif "ds" in user_input or "data structure" in user_input:
        print("DreamBuddy: Data Structures are the foundation of coding. Start with arrays, then move to linked lists!")

    elif "ai" in user_input or "artificial intelligence" in user_input:
        print("DreamBuddy: AI is transforming the world! Learn Python, math, and explore machine learning algorithms.")

    elif "thank" in user_input:
        print("DreamBuddy: You're most welcome! 💙 Keep going!")

    elif "bye" in user_input:
        print("DreamBuddy: Bye! Stay consistent and keep pushing toward your goals! 🌟")
        break

    else:
        print("DreamBuddy: Hmm, I’m not sure how to respond to that. Try asking something related to studies! 📚")