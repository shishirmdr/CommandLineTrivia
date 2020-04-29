import html
import random


class Question:
    def __init__(self, prop):
        self.category   = prop["category"]
        self.kind       = prop["type"]
        self.question   = html.unescape(prop['question'])
        self.correct    = prop['correct_answer']
        self.incorrects = prop['incorrect_answers']
        self.answers    = [self.correct] + self.incorrects

        self.answers.sort(reverse=True)
        # shuffle mutliple choice questions
        if self.kind == "multiple":
            random.shuffle(self.answers)

    def show(self):
        print("Category:", self.category)
        print(self.question)

        for i, answer in enumerate(self.answers):
            print(f"{i + 1}. {html.unescape(answer)}")

    def isCorrect(self, ans):
        correct_ind = self.answers.index(self.correct)

        # raises ValueError
        ans = int(ans) - 1
        if (ans < 0) or (ans >= len(self.answers)):
            raise ValueError

        if ans == correct_ind:
            return True

        return False


class QuestionList:
    def __init__(self, questions):
        self.qlist = questions

    def __iter__(self):
        for q in self.qlist:
            yield Question(q)
