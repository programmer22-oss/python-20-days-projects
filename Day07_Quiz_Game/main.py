quiz = {
    "What is the capital of India?": "delhi",
    "Which language is used for web apps?": "python",
    "What does CPU stand for?": "central processing unit",
    "Which keyword is used to define a function in Python?": "def"
}

score = 0

print("🧠 Welcome to the Quiz Game\n")

for question, answer in quiz.items():
    print(question)
    user_answer = input("Your answer: ").lower()

    if user_answer == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is: {answer}\n")

print(f"🎯 Your final score: {score}/{len(quiz)}")
if score == len(quiz):
    print("🏆 Excellent! You got all answers correct!")
elif score >= len(quiz) / 2:
    print("👍 Good job! You passed the quiz.")
else:
    print("😞 Better luck next time!")
    