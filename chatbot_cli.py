def run_chatbot():

	print("write Exit to quit")

	responses = {
		"hello" : "how can i help you?",
		"how are you" : "i am a computer program, but thanks"
	}

	while True:
		user_input = input("you: ")
		cleaned_input = user_input.lower().strip()

		if cleaned_input == "exit":
            			print("chatbot: have a good day")
            			break

		bot_response = responses.get(cleaned_input, "sorry, can you ask another question?")
		print(f"chatbot: {bot_response}")

if __name__ == "__main__":
	run_chatbot()