import random
import sys  # per usare sys.exit()

class QuizBrain:

    def __init__(self, q_list):
        self.user_score = 0
        self.question_list = q_list
        self.question_number = 0
        self.question_index = random.randint(0,50)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_index]
        self.question_number += 1
        self.question_index = random.randint(0,50)
        print(current_question.category)
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?\n").lower()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right! ")
            self.user_score += 1
        else:
            print("That's wrong! ")
            print(f"The correct answer was {correct_answer}. ")
            input("\nPlease press ENTER to close the program... ")
            sys.exit() # <--- Interrompe il programma qui
        print(f"Il tuo punteggio attuale è: {self.user_score}/{self.question_number}")
        print("\n")

