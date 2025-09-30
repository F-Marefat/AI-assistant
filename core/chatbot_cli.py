#core/chatbot_cli.py

from .responses import RESPONSES_DATA

def run_chatbot():

	print("write Exit to quit")

	responses = RESPONSES_DATA

	while True:
		try:
			user_input = input("you: ")
			cleaned_input = user_input.lower().strip()

			if cleaned_input == "exit":
            			print("chatbot: have a good day")
            			break

			bot_response = responses.get(cleaned_input, "sorry, can you ask another question?")
			print(f"chatbot: {bot_response}")
		except KeyboardInterrupt:
			print("exit on your command")
		except Exception as e:
			print(f"unxpected error : {e}")
			break

if __name__ == "__main__":
	run_chatbot()