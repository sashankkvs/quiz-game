from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question  = Question(question_text, question_answer)
    question_bank.append(new_question)

quizz = Quizbrain(question_bank)
while quizz.still_has_questions():
    quizz.next_question()
print("You have finished the quizz")
print(f"Your score is {quizz.score}/{quizz.question_numTrueber}")