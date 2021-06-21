from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Create a list of Question objects and stored in the list: question_bank
# Loop through each element in question_data
# for each question and answer, create a Question object
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

# Create a QuizBrain object
quiz = QuizBrain(question_bank)

while quiz.still_have_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")


