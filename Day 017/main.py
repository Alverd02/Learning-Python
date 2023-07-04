from question_model import question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    q = question(i["text"], i["answer"])
    question_bank.append(q)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()
    print("\n")
