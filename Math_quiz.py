import random
import time


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer


def main():
    score = 0
    timeout = 10
    quiz_count = 5
    for _ in range(quiz_count):
        question, correct_answer = generate_question()
        print(f"question: {question}")

        start_time = time.time()
        user_answer = input(" enter your answer: ")

        try:
            user_answer = int(user_answer)
        except ValueError:
            print("invalid number!")
            continue

        elapsed_time = time.time() - start_time

        if elapsed_time < timeout:
            if user_answer == correct_answer:
                score += 1
                print("Correct answer! Your score:", score)
            else:
                print(f"wrong answer! Correct answer: {correct_answer}")
        else:
            print("Time is up! next question...")
    print(f"FINAL SCORE: {score} out of{quiz_count}")


if __name__ == "__main__":
    main()





