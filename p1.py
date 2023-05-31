import os

class Agent:
    def __init__(self):
        self.files = {}
        self.default_answer = "I'm sorry, I don't have an answer for that."

    def upload_file(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                content = file.read()
                self.files[file_name] = content
                print(f"File '{file_name}' uploaded successfully.")
        else:
            print(f"File '{file_name}' does not exist.")

    def ask_question(self, question):
        for content in self.files.values():
            if question in content:
                return self.extract_answer(content, question)
        return self.default_answer

    def extract_answer(self, content, question):
        # Extract the answer from the content based on some logic
        # You can use NLP techniques, regex, or any other method suitable for your use case
        # Here's a simple example that returns the first line containing the question as the answer
        lines = content.split('\n')
        for line in lines:
            if question in line:
                return line
        return self.default_answer

# Usage example
agent = Agent()

# Upload files
agent.upload_file("file1.txt")
agent.upload_file("file2.txt")

# Ask questions
question1 = "What is the capital of France?"
answer1 = agent.ask_question(question1)
print(answer1)

question2 = "Who is the CEO of Apple?"
answer2 = agent.ask_question(question2)
print(answer2)
