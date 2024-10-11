'''
    - Write a program to create a class that models a simple quiz system 
      with methods to add, remove, and display questions.
'''

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def __str__(self):
        return f"Question: {self.question}\nOptions: {self.options}\nAnswer: {self.answer}"

class QuizSystem:
    def __init__(self):
        self.questions = []

    def add_question(self, question, options, answer):
        new_question = Question(question, options, answer)
        self.questions.append(new_question)
        print(f"Question added: {question}")

    def remove_question(self, question_number):
        try:
            question_number = int(question_number)
            if 1 <= question_number <= len(self.questions):
                del self.questions[question_number - 1]
                print(f"Question {question_number} removed")
            else:
                print("Invalid question number")
        except ValueError:
            print("Invalid input")

    def display_questions(self):
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}:")
            print(question)
            print("--------------------")

    def quiz(self):
        score = 0
        for i, question in enumerate(self.questions, start=1):
            print(f"Question {i}:")
            print(question.question)
            for j, option in enumerate(question.options, start=1):
                print(f"{j}. {option}")
            answer = input("Enter answer number: ")
            if question.options[int(answer) - 1] == question.answer:
                score += 1
                print("Correct!")
            else:
                print(f"Wrong! Correct answer: {question.answer}")
        print(f"Quiz finished. Your score: {score}/{len(self.questions)}")

# Example usage
quiz_system = QuizSystem()

while True:
    print("\nQuiz System")
    print("1. Add question")
    print("2. Remove question")
    print("3. Display questions")
    print("4. Take quiz")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        question = input("Enter question: ")
        options = input("Enter options (comma-separated): ").split(',')
        options = [option.strip() for option in options]
        answer = input("Enter answer: ")
        quiz_system.add_question(question, options, answer)
    elif choice == "2":
        question_number = input("Enter question number to remove: ")
        quiz_system.remove_question(question_number)
    elif choice == "3":
        quiz_system.display_questions()
    elif choice == "4":
        quiz_system.quiz()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
