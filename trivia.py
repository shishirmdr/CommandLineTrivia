import requests
from question import QuestionList
import colorama as color


class Trivia:
    URL = "https://opentdb.com/api.php"

    def __init__(self, amount, difficulty):
        color.init()

        self.amount = amount
        self.res = requests.get(self.URL, params={'amount': self.amount,
                                'difficulty': difficulty}).json()
        self.score = 0

    def begin(self):
        qlist = QuestionList(self.res['results'])

        for q in qlist:
            while True:
                q.show()
                try:
                    if q.isCorrect(input("ans: ")):
                        self.score += 1
                    break
                except (ValueError):
                    print(color.Fore.RED)
                    print('Not a valid answer! enter again...')
                    print(color.Style.RESET_ALL)

            print()

        self.show_end_score()

    def show_end_score(self):
        print(color.Fore.GREEN)
        print(f"You scored {self.score} out of {self.amount}.")
        print(color.Style.RESET_ALL)
