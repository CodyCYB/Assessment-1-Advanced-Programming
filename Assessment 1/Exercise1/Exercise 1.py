import random

def menu():
    print("Math Quiz!")
    print("Choose a Difficulty Level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("enter your choice (1-3): ").strip()
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Invalid choice. Please enter a number between 1 and 3.")

def get_numbers(level):
    if level == 1:
        return random.randint(1, 10), random.randint(1, 10)
    elif level == 2:
        return random.randint(10, 100), random.randint(10, 100)
    else:
        return random.randint(100, 1000), random.randint(100, 1000)

def choose_operation():
    return random.choice(["+", "-"])

def ask_question(num1, num2, operation):
    correct_answer = num1 + num2 if operation == "+" else num1 - num2
    for attempt in (1, 2):
        while True:
            try:
                answer = int(input(f"What is {num1} {operation} {num2}? "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        if answer == correct_answer:
            if attempt == 1:
                print("Correct! First try — +10 points")
                return 10
            else:
                print("Correct! Second try — +5 points")
                return 5
        else:
            if attempt == 1:
                print("Incorrect. Try again.")
            else:
                print(f"Incorrect. The correct answer is {correct_answer}.")
                return 0
    return 0

def results(total_score):
    print(f"\nYour total score is: {total_score}/100 points")
    if total_score >= 90:
        grade = "A"
    elif total_score >= 80:
        grade = "B"
    elif total_score >= 70:
        grade = "C"
    elif total_score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Grade: {grade}\n")

def quiz():
    level = menu()
    total_score = 0
    for i in range(10):
        num1, num2 = get_numbers(level)
        operation = choose_operation()
        points = ask_question(num1, num2, operation)
        total_score += points
    results(total_score)

def main():
    print("Welcome to the Math Quiz")
    while True:
        quiz()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()