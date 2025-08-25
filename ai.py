import time

class SimpleBot:
    def __init__(self, name="StarterBot"):
        self.name = name

    def greet(self):
        print(f"Hello! I am {self.name}. How can I help you today?")

    def process_command(self, command):
        command = command.lower().strip()
        if command in ["hi", "hello"]:
            return "Hi there! How can I assist you?"
        elif command in ["time", "what time is it?"]:
            return f"The current time is {time.strftime('%Y-%m-%d %H:%M:%S')}"
        elif command in ["bye", "exit", "quit"]:
            return "Goodbye! Have a great day!"
        else:
            return "Sorry, I don't understand that command."

    def run(self):
        self.greet()
        while True:
            user_input = input("> ")
            response = self.process_command(user_input)
            print(response)
            if user_input.lower().strip() in ["bye", "exit", "quit"]:
                break

if __name__ == "__main__":
    bot = SimpleBot()
    bot.run()
