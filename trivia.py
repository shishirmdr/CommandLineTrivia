import requests
from question import Question


class Trivia:
    URL = "https://opentdb.com/api.php"

    def __init__(self, amount, difficulty):
        self.amount = amount
        self.res = requests.get(self.URL,
                                params={'amount': self.amount,
                                'difficulty': difficulty}).json()
        self.score = 0

    def begin(self):
        for question in self.questions():
            while True:
                question.show()
                try:
                    if question.isCorrect(input("ans: ")):
                        self.score += 1
                    break
                except ValueError:
                    print('Not a valid answer! enter again...\n')

            print()

        self.show_end_score()

    def questions(self):
        for i in range(self.amount):
            yield Question(self.res['results'][i])

    def show_end_score(self):
        greetings = "Congrats" if (self.score >= self.amount/2) else "Too bad"
        print(f"{greetings}! you scored {self.score} out of {self.amount}.")
